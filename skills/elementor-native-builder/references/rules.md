# Rules

## Authority and evidence

- Read repository instructions and the current implementation before acting.
- Use official Elementor developer documentation and the installed
  Elementor/Pro source for integration details. Never rely on remembered
  control names or JSON keys.
- Confirm the active child theme, Elementor experiments/features, Pro
  availability, language plugin, cache/CDN, and deployed paths.
- Distinguish diagnosis from implementation. If the user asks only for the
  problem, report the cause and evidence before changing anything.

## Native and editable

- Use stock Elementor/Pro widgets whenever they can express the requirement.
- On an existing Elementor site, make every layout change through the native
  Elementor editor/model, one section or Theme Builder document per save.
- Never use a custom builder or mutation script, WP-CLI seeder, bulk import,
  bulk database edit, direct `_elementor_data` write, or global search-and-
  replace to align an existing design.
- Never substitute a large page-specific CSS parity layer for native container,
  widget, Site Settings, or responsive controls.
- Use Loop Item plus Loop Grid/Carousel for repeated cards.
- Use Elementor Pro Form actions and Submissions instead of a custom endpoint,
  lead post type, or frontend handler.
- Register a custom Elementor widget only for genuinely unsupported dynamic
  rendering. Give it editor controls, escaping, stable naming, and dependency
  declarations.
- Raw HTML and Shortcode widgets require a written reason and explicit user
  approval. Record approved exceptions in the final audit.

## Data and security

- Sanitize on write, escape on output, verify nonces, and enforce capabilities.
- Use prepared queries and WordPress APIs. Do not trust request, meta, or term
  input.
- Make translation relationships explicit. Do not allow language-plugin sync
  settings to overwrite translated post meta or taxonomies.
- Never put credentials, passwords, private keys, or production dumps in the
  plugin, generated reports, screenshots, or git.

## Change safety

- Preserve unrelated working-tree and production changes.
- Resolve exact document IDs, post IDs, option keys, and remote paths before
  mutation.
- Back up the complete target document and record hashes before editor changes.
- Edit, add, duplicate, move, and delete through Elementor's editor or Navigator
  so Elementor generates IDs and persists parent/order relationships.
- Save after one bounded section/template change, reopen the editor, and verify
  both the rendered frontend and the resulting JSON structure before continuing.
- Keep the last known-good document export available until all required
  breakpoints pass.
- Flush Elementor/CSS caches only after the bounded write succeeds.
- Never claim a backup exists unless its path, size, and restore command are
  verified.

## Validation discipline

- Do not generate or run unit tests unless the user explicitly requests them.
- Run syntax checks only on modified files by default.
- Use Playwright to exercise the actual route and the Elementor editor.
- Browser JavaScript must remain read-only measurement code. Do not inject or
  persist DOM, CSS, or JavaScript as an implementation shortcut.
- Wait for `document.fonts.ready` before visual measurements.
- Compare header, footer, and each section independently at desktop, tablet, and
  mobile, including inner containers, widgets, text metrics, padding, gaps,
  media crops, and interaction states.
- Treat database rows, successful HTTP codes, and screenshots as different
  evidence; one does not replace the others.
- Do not call a page pixel-perfect without a reference render, matching
  viewport, and measured or visual comparison.
