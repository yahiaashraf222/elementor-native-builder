# Elementor implementation

## Use version evidence

Elementor stores page structure as JSON-backed post metadata, but widget and
control schemas change. Before editing:

1. read the installed widget registration and control definitions;
2. export a small known-good template from the same installation when useful;
3. confirm feature flags such as Containers or Atomic Widgets;
4. render a staging document and reopen it in the editor.

Official starting points:

- https://developers.elementor.com/docs/data-structure/
- https://developers.elementor.com/docs/data-structure/responsive-data/
- https://developers.elementor.com/docs/widgets/
- https://developers.elementor.com/docs/dynamic-tags/
- https://developers.elementor.com/docs/themes/

## Documents and locations

- Create the correct Elementor document type for headers, footers, Loop Items,
  singles, archives, and pages.
- Save and verify display conditions with the installed Pro implementation.
- Confirm the active theme calls Elementor theme locations.
- Use a page template that renders theme locations when header/footer output is
  expected; do not choose Canvas accidentally.
- Verify the location server-side and through the public route.

Do not write `_elementor_data` directly for existing-site design alignment.
Use it only as a backed-up, read-only verification artifact after Elementor
saves the document.

## Responsive editor data

- Verify the installed control names and value shapes before editing.
- In classic Elementor data, a responsive control stores desktop in the base
  key and device overrides beside it, such as `control_name_tablet` and
  `control_name_mobile`.
- Additional breakpoints use their configured device suffixes. Atomic Widgets
  may use style variants instead, so inspect the installed feature state and a
  known-good editor save before relying on either shape.
- Set responsive values through Elementor's responsive editor controls. After
  saving, inspect the exact element settings and confirm inheritance at every
  required breakpoint.

## Native widgets and classes

- Containers own layout; widgets own content and interaction.
- In the classic Elementor structure, container classes use `css_classes` and
  widget classes use `_css_classes`. Confirm this against the installed
  version, especially with Atomic Widgets.
- Style native markup below the assigned class, such as a Heading widget’s
  `.elementor-heading-title` or a Button widget’s `.elementor-button`.
- Use dual selectors only during a bounded migration, then remove legacy
  selectors once the audit proves no legacy structure remains.

## Repeated and dynamic content

- Prefer Loop Item documents and Loop Grid/Carousel query controls.
- Confirm query control keys from installed Pro source; never guess prefixes.
- Let the language plugin filter loops only after proving its query behavior.
- Register dynamic tags through Elementor’s supported manager hook.
- Use custom widgets for repeater-heavy renderers only when stock widgets and
  dynamic tags cannot expose the structure cleanly.

## Forms

- Use Elementor Pro Form when available.
- Read the installed Form widget and actions before serializing field repeaters,
  email settings, localized messages, or submission actions.
- Verify both email and database storage. Setting an explicit action list can
  remove a default storage action.
- Use a throwaway submission, confirm values and Reply-To behavior, review
  browser errors, then delete the test data.

## CSS and responsive behavior

- Prefer native container/widget controls and Site Settings over child-theme
  layout CSS.
- Do not create a large CSS layer that absolutely positions or force-sizes page
  sections to imitate a screenshot.
- Elementor containers are flex by default. Explicitly set row/grid direction
  and gaps when the reference requires them.
- A base rule using `!important` needs an equal-or-stronger responsive override.
- Avoid a `background` shorthand that erases a native background image; change
  only the needed property.
- Inspect lazy-background rules when images appear only after scrolling.
- Elementor may force `.e-con::before` to absolute positioning. When a pseudo
  must participate in flex/grid flow, verify and override its position.
- Inspect Accordion icon floats and dimensions when circles collapse to ovals.
- Reopen hamburger menus, carousels, accordions, and forms at every responsive
  breakpoint; static screenshots do not prove their behavior.

## Multilingual behavior

- Link translated pages and Theme Builder templates explicitly.
- Verify AR and EN use the intended template, menu, typography, and query.
- Review language-plugin sync settings before writing meta or terms. Apply
  sync-setting changes and translated content writes in separate requests when
  the plugin caches configuration.
- Check RTL placement using actual computed flex order, not visual assumptions.
