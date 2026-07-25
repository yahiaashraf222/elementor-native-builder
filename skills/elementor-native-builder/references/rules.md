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
- Back up the complete target and record hashes before direct Elementor meta,
  options, templates, or production files are replaced.
- Prefer patching a stable child-theme stylesheet over rebuilding a template
  that contains manual editor changes.
- Flush Elementor/CSS caches only after the bounded write succeeds.
- Never claim a backup exists unless its path, size, and restore command are
  verified.

## Validation discipline

- Do not generate or run unit tests unless the user explicitly requests them.
- Run syntax checks only on modified files by default.
- Exercise the actual route and affected interaction in a browser.
- Wait for `document.fonts.ready` before visual measurements.
- Treat database rows, successful HTTP codes, and screenshots as different
  evidence; one does not replace the others.
- Do not call a page pixel-perfect without a reference render, matching
  viewport, and measured or visual comparison.
