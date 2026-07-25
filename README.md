# Native Elementor Builder

A Codex and Claude Code plugin for reproducing reference designs as editable,
dynamic Elementor/Elementor Pro sites with strict safety and verification
gates.

The bundled `elementor-native-builder` skill enforces:

- native Elementor/Pro widgets before custom HTML or shortcodes;
- Loop Item and Loop Grid architecture for repeated content;
- safe, version-aware programmatic Elementor document generation;
- protected CPT/meta and multilingual RTL/LTR handling;
- page-by-page responsive visual comparison;
- backups, rollback boundaries, structural audits, and evidence-based handoff.

## Install in Codex

```bash
codex plugin marketplace add yahiaashraf222/elementor-native-builder --ref main
codex plugin add elementor-native-builder@elementor-native-builder
```

Start a new Codex thread, then invoke `$elementor-native-builder` or ask Codex
to rebuild or audit an Elementor site.

## Install in Claude Code

```bash
claude plugin marketplace add yahiaashraf222/elementor-native-builder
claude plugin install elementor-native-builder@elementor-native-builder
```

Run `/reload-plugins`, then invoke:

```text
/elementor-native-builder:elementor-native-builder
```

Claude Code namespaces plugin skills with the plugin name.

## Validate a checkout

```bash
python scripts/validate_repository.py
python skills/elementor-native-builder/scripts/audit_elementor_json.py path/to/elementor-export.json
claude plugin validate . --strict
```

Codex metadata can additionally be checked with Codex’s plugin validator when
developing inside Codex.

## Safe default

The workflow does not create or run unit tests unless the user explicitly asks.
It uses modified-file syntax checks, structural Elementor audits, real route and
interaction checks, and multi-breakpoint browser verification by default.
