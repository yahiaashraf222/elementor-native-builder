---
name: elementor-native-builder
description: Build, refactor, diagnose, or verify WordPress sites implemented with Elementor or Elementor Pro from reference designs. Use for native-widget conversions, Theme Builder templates, Loop Grid and Loop Item systems, dynamic CPT content, bilingual RTL/LTR sites, programmatic Elementor JSON generation, responsive pixel-parity work, or audits of HTML and Shortcode widget usage.
---

# Native Elementor Builder

Build the result as a client-editable Elementor site and prove it against the
reference. Treat a visually similar screenshot as insufficient when the
structure is not editable, dynamic, responsive, or safe to rebuild.

## Mandatory sequence

1. Read [rules.md](references/rules.md) before changing files, WordPress, or
   Elementor data.
2. Inspect the repository instructions, installed theme/plugins and versions,
   current Elementor documents, existing content model, language plugin, and
   deployment path. Do not infer any of them.
3. Read [workflow.md](references/workflow.md) and define the reference contract,
   page matrix, breakpoints, dynamic model, and safe implementation boundary.
4. Read [elementor-implementation.md](references/elementor-implementation.md)
   before generating Elementor data, registering widgets/tags, or creating Theme
   Builder and Loop templates.
5. Implement in small, reversible slices. Preserve user edits and unrelated
   work. Back up the exact target before replacing generated documents.
6. Read [verification.md](references/verification.md), run every applicable
   gate, and report evidence page by page.
7. Consult [failure-modes.md](references/failure-modes.md) when visual geometry,
   multilingual content, form storage, backgrounds, or template discovery
   behaves unexpectedly.

## Native-first decision order

Use the first viable option:

1. Elementor or Elementor Pro stock widget.
2. Theme Builder, Loop Grid/Carousel, Loop Item, dynamic tag, or native query.
3. A registered custom Elementor widget with controls and editor visibility.
4. Raw HTML, a Shortcode widget, or bespoke frontend handler only when the
   installed stack has no reasonable native equivalent and the user explicitly
   approves the exception.

Never replace Elementor Pro Form, Accordion, Nav Menu, Loop Grid, Counter,
Image, Heading, Text Editor, Button, Icon List, or similar stock capabilities
with custom markup merely because coding is faster.

## Implementation contract

- Keep layout in Elementor containers and content in Elementor widgets.
- Put reusable visual rules in the active child theme, using stable classes on
  containers and widgets. Keep text, links, media, form fields, and queries
  editable in Elementor.
- Use dynamic content for repeated entities. Prefer CPTs, protected meta,
  taxonomies, Loop Items, and language-aware queries over duplicated cards.
- Inspect the installed Elementor/Pro source or export a known-good sample
  before using version-specific widget types, control keys, actions, document
  types, conditions, or JSON shapes.
- Treat `_elementor_data` as an internal, version-sensitive contract. Back it
  up, hash it, and verify a staging render before any bounded direct write.
- Do not recreate generated templates over manual editor changes without
  showing the user the exact overwrite boundary.
- Do not create or run unit tests unless the user explicitly requests them.
  By default run syntax checks, structural audits, and real runtime/browser
  verification only.

## Required gates

Do not call work complete until all applicable gates pass:

- **Preflight:** stack, versions, theme locations, languages, reference assets,
  credentials path, and target environment are confirmed.
- **Safety:** backup/rollback artifact exists for every replaced document or
  production file; unrelated changes remain untouched.
- **Structure:** no unjustified HTML or Shortcode widgets; unique element IDs;
  correct container/widget class keys; dynamic loops use the intended query.
- **Syntax:** check only modified PHP/JS/CSS files with the project-supported
  tools. Do not run unrelated full-repository or unit-test suites.
- **Runtime:** routes return expected content, Theme Builder locations render,
  forms and dynamic templates work, and browser console/network failures are
  reviewed.
- **Visual:** compare reference and implementation after fonts load at every
  required breakpoint in both LTR and RTL. Measure concrete DOM geometry when
  screenshots disagree.
- **Responsive:** verify no horizontal overflow, correct grid collapse, menu
  behavior, forms, carousels, and footer layout at desktop, tablet, and mobile.
- **Handoff:** give exact pages, widths, commands, screenshots, counts, and any
  approved exceptions. Do not say “pixel-perfect” without evidence.

## Structural audit helper

Audit exported Elementor JSON or captured `_elementor_data`:

```bash
python skills/elementor-native-builder/scripts/audit_elementor_json.py path/to/export.json
```

Use `--strict-shortcodes` when raw shortcode-like content is forbidden. Use
`--allow-widget` only for a documented, user-approved exception. A nonzero exit
means the structure gate failed.
