#!/usr/bin/env python3
"""Validate cross-compatible plugin metadata and internal skill references."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "elementor-native-builder"
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDER = "[" + "TODO:"


def load_json(relative: str) -> dict[str, Any]:
    path = ROOT / relative
    if not path.is_file():
        raise ValueError(f"missing {relative}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {relative}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{relative} must contain a JSON object")
    return value


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_skill(errors: list[str]) -> None:
    skill = ROOT / "skills" / PLUGIN_NAME / "SKILL.md"
    require(skill.is_file(), f"missing {skill.relative_to(ROOT)}", errors)
    if not skill.is_file():
        return
    text = skill.read_text(encoding="utf-8")
    require(PLACEHOLDER not in text, "SKILL.md contains a TODO placeholder", errors)
    frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    require(frontmatter is not None, "SKILL.md frontmatter is missing", errors)
    if frontmatter:
        lines = [
            line for line in frontmatter.group(1).splitlines() if line.strip()
        ]
        keys = [line.split(":", 1)[0].strip() for line in lines if ":" in line]
        require(keys == ["name", "description"], "SKILL.md must have only name and description frontmatter", errors)
        require(
            any(line == f"name: {PLUGIN_NAME}" for line in lines),
            "SKILL.md name does not match the plugin",
            errors,
        )

    for target in LINK_RE.findall(text):
        if "://" in target or target.startswith("#"):
            continue
        resolved = (skill.parent / target).resolve()
        require(
            resolved.is_relative_to(skill.parent.resolve()) and resolved.exists(),
            f"broken skill link: {target}",
            errors,
        )


def validate_manifests(errors: list[str]) -> None:
    codex = load_json(".codex-plugin/plugin.json")
    claude = load_json(".claude-plugin/plugin.json")
    claude_market = load_json(".claude-plugin/marketplace.json")
    codex_market = load_json(".agents/plugins/marketplace.json")

    for label, manifest in (("Codex", codex), ("Claude", claude)):
        require(manifest.get("name") == PLUGIN_NAME, f"{label} manifest name mismatch", errors)
        version = manifest.get("version")
        require(isinstance(version, str) and bool(VERSION_RE.match(version)), f"{label} version is not strict semver", errors)
        require(manifest.get("skills") == "./skills/", f"{label} skills path mismatch", errors)
        require(
            manifest.get("repository") == f"https://github.com/yahiaashraf222/{PLUGIN_NAME}",
            f"{label} repository URL mismatch",
            errors,
        )

    versions = {
        codex.get("version"),
        claude.get("version"),
        claude_market.get("metadata", {}).get("version"),
        claude_market.get("plugins", [{}])[0].get("version"),
    }
    require(len(versions) == 1, "manifest and marketplace versions differ", errors)

    claude_plugins = claude_market.get("plugins")
    require(isinstance(claude_plugins, list) and len(claude_plugins) == 1, "Claude marketplace must expose one plugin", errors)
    if isinstance(claude_plugins, list) and claude_plugins:
        require(claude_plugins[0].get("name") == PLUGIN_NAME, "Claude marketplace plugin name mismatch", errors)
        require(claude_plugins[0].get("source") == "./", "Claude marketplace source must be ./", errors)

    codex_plugins = codex_market.get("plugins")
    require(isinstance(codex_plugins, list) and len(codex_plugins) == 1, "Codex marketplace must expose one plugin", errors)
    if isinstance(codex_plugins, list) and codex_plugins:
        entry = codex_plugins[0]
        require(entry.get("name") == PLUGIN_NAME, "Codex marketplace plugin name mismatch", errors)
        require(entry.get("source") == {"source": "local", "path": "."}, "Codex marketplace source must be repository root", errors)
        policy = entry.get("policy", {})
        require(policy.get("installation") == "AVAILABLE", "Codex installation policy mismatch", errors)
        require(policy.get("authentication") == "ON_INSTALL", "Codex authentication policy mismatch", errors)


def validate_repository(errors: list[str]) -> None:
    required = [
        "README.md",
        "LICENSE",
        "skills/elementor-native-builder/scripts/audit_elementor_json.py",
        ".github/workflows/validate.yml",
    ]
    for relative in required:
        require((ROOT / relative).is_file(), f"missing {relative}", errors)

    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml", ".yml", ".py"}:
            text = path.read_text(encoding="utf-8")
            require(PLACEHOLDER not in text, f"placeholder in {path.relative_to(ROOT)}", errors)


def main() -> int:
    errors: list[str] = []
    try:
        validate_manifests(errors)
        validate_skill(errors)
        validate_repository(errors)
    except ValueError as exc:
        errors.append(str(exc))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {PLUGIN_NAME} repository metadata and skill wiring are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
