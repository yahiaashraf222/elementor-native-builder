# Verification

## Gate 0: preflight

- Record WordPress, PHP, Elementor, Pro, theme, and language-plugin versions.
- Confirm reference source, route matrix, viewports, and expected interactions.
- Confirm staging versus production and the authorized write boundary.
- Record current git status and unrelated changes.

## Gate 1: rollback

- Back up each Elementor document/meta value and modified production file.
- Record target ID/path, byte size, timestamp, and SHA-256.
- Write and verify the restore command before mutation.
- For generated-template rebuilds, identify manual editor changes first.

## Gate 2: structure

- Export or capture the editor-saved Elementor JSON.
- Run `scripts/audit_elementor_json.py`.
- Require unique IDs and zero unapproved HTML or Shortcode widgets.
- Confirm native widget types, Loop Item IDs, queries, document conditions, and
  language relationships.
- Confirm every added/duplicated element has an Elementor-generated unique ID
  and every moved element has the intended parent and sibling order.
- Confirm responsive control keys/variants match the installed Elementor
  version and the values set in the editor.
- Reopen representative documents in Elementor editor.

## Gate 3: syntax and server render

- Run syntax checks only for modified PHP and JavaScript files.
- Do not create/run unit tests without an explicit user request.
- Flush rewrite rules only when rewrite behavior changed.
- Clear Elementor generated CSS/files after successful document changes.
- Confirm server-side Theme Builder locations produce non-empty output.

## Gate 4: route and interaction

For every page and language:

- confirm status, title, canonical content, expected section count, and no
  archive/page slug collision;
- review browser console errors, failed requests, and missing assets;
- open navigation, accordions, sliders, tabs, and mobile menus;
- submit forms with disposable data, verify storage/email, and remove it;
- verify dynamic cards and singles use the correct language and entity.

## Gate 5: visual parity

At the approved widths:

1. render the reference over HTTP, not `file://`, if browser restrictions apply;
2. load the implementation with cache-busting when a CDN is present;
3. wait for `document.fonts.ready`;
4. capture matching full-page screenshots and one focused screenshot for the
   header, footer, and every section;
5. compare section order, bounds, type, colors, spacing, crops, and states;
6. inspect `getBoundingClientRect()` and `getComputedStyle()` on the section,
   inner containers, headings, text, buttons, media, and interactive widgets;
7. fix one Elementor section/template, save it, then rerun all three viewport
   checks before continuing to the next section.

A matching section height or outer rectangle does not pass when internal
typography, padding, gaps, alignment, or media treatment differs.

At minimum cover desktop, tablet, and mobile. Typical diagnostic widths are
1440/1280, 1024, 820/768, 600, and 390/375, but the reference contract governs.

For RTL/LTR, verify both rather than assuming mirroring.

## Gate 6: responsive integrity

At each width, assert:

- `scrollWidth <= clientWidth`;
- grids collapse to the expected columns;
- text does not clip or overflow;
- controls remain tappable;
- header logo, language switcher, and hamburger group correctly;
- footer navigation does not become an unintended hamburger;
- forms and cards retain intended widths;
- background media and overlays remain legible.

## Gate 7: delivery evidence

Report:

- exact commits/files/templates changed;
- native widget, custom widget, HTML widget, and Shortcode widget counts;
- page/language/viewport matrix with pass/fail;
- screenshots or comparison artifact paths;
- console/network/form results;
- rollback artifact and restore command;
- approved exceptions and remaining risk.

If any required gate is unverified, label the result incomplete or blocked.
