#!/usr/bin/env python3
"""Audit exported Elementor JSON for structural native-widget guardrails."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


SHORTCODE_RE = re.compile(r"\[(?!/?(?:caption|gallery)\b)[A-Za-z][\w-]*(?:\s[^\]]*)?\]")
DEFAULT_FORBIDDEN = {"html", "shortcode"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit Elementor export or _elementor_data JSON."
    )
    parser.add_argument("paths", nargs="+", help="JSON files/directories, or - for stdin")
    parser.add_argument(
        "--allow-widget",
        action="append",
        default=[],
        metavar="TYPE",
        help="Allow a normally forbidden widget type; repeat as needed.",
    )
    parser.add_argument(
        "--strict-shortcodes",
        action="store_true",
        help="Treat shortcode-like strings as errors instead of warnings.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format.",
    )
    return parser.parse_args()


def iter_json_sources(paths: Iterable[str]) -> Iterable[tuple[str, Any]]:
    stdin_used = False
    for raw in paths:
        if raw == "-":
            if stdin_used:
                raise ValueError("stdin may be specified only once")
            stdin_used = True
            yield "<stdin>", json.load(sys.stdin)
            continue

        path = Path(raw)
        if not path.exists():
            raise FileNotFoundError(path)
        files = sorted(path.rglob("*.json")) if path.is_dir() else [path]
        if not files:
            raise ValueError(f"no JSON files found under {path}")
        for file_path in files:
            with file_path.open("r", encoding="utf-8-sig") as handle:
                yield str(file_path), json.load(handle)


def walk(value: Any, json_path: str = "$") -> Iterable[tuple[str, Any]]:
    yield json_path, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, f"{json_path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{json_path}[{index}]")


def audit_document(label: str, document: Any, allowed: set[str], strict: bool) -> dict[str, Any]:
    widgets: Counter[str] = Counter()
    ids: dict[str, list[str]] = {}
    errors: list[str] = []
    warnings: list[str] = []
    element_count = 0

    for json_path, value in walk(document):
        if isinstance(value, dict) and isinstance(value.get("elType"), str):
            element_count += 1
            element_id = value.get("id")
            if isinstance(element_id, str) and element_id:
                ids.setdefault(element_id, []).append(json_path)

            settings = value.get("settings")
            if not isinstance(settings, dict):
                settings = {}

            el_type = value["elType"]
            if el_type == "widget":
                widget_type = value.get("widgetType")
                if not isinstance(widget_type, str) or not widget_type:
                    errors.append(f"{json_path}: widget has no widgetType")
                else:
                    widgets[widget_type] += 1
                    if widget_type in DEFAULT_FORBIDDEN and widget_type not in allowed:
                        errors.append(f"{json_path}: forbidden widget type {widget_type!r}")
                if "css_classes" in settings and "_css_classes" not in settings:
                    errors.append(
                        f"{json_path}: classic widget uses css_classes; expected _css_classes"
                    )
            elif el_type == "container":
                if "_css_classes" in settings and "css_classes" not in settings:
                    errors.append(
                        f"{json_path}: classic container uses _css_classes; expected css_classes"
                    )

        if isinstance(value, str) and SHORTCODE_RE.search(value):
            message = f"{json_path}: shortcode-like content {value[:120]!r}"
            (errors if strict else warnings).append(message)

    for element_id, locations in sorted(ids.items()):
        if len(locations) > 1:
            errors.append(
                f"duplicate element id {element_id!r}: " + ", ".join(locations)
            )

    return {
        "source": label,
        "elements": element_count,
        "widgets": dict(sorted(widgets.items())),
        "errors": errors,
        "warnings": warnings,
    }


def render_text(results: list[dict[str, Any]]) -> None:
    for result in results:
        print(f"{result['source']}: {result['elements']} elements")
        widget_summary = ", ".join(
            f"{name}={count}" for name, count in result["widgets"].items()
        )
        print(f"  widgets: {widget_summary or 'none'}")
        for error in result["errors"]:
            print(f"  ERROR: {error}")
        for warning in result["warnings"]:
            print(f"  WARNING: {warning}")
        if not result["errors"] and not result["warnings"]:
            print("  PASS")


def main() -> int:
    args = parse_args()
    allowed = set(args.allow_widget)
    try:
        results = [
            audit_document(label, document, allowed, args.strict_shortcodes)
            for label, document in iter_json_sources(args.paths)
        ]
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"audit input error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        render_text(results)

    return 1 if any(result["errors"] for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
