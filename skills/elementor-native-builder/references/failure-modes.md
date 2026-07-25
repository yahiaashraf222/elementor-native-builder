# Failure modes

## Empty or undiscoverable templates

- A raw WordPress post may not be recognized as an Elementor Theme Builder
  document. Create the installed document type through the supported document
  manager and verify `get_document()`.
- A page using Elementor Canvas omits theme header/footer locations. Use the
  intended template and verify the location output.
- Display conditions are version-specific. Read the installed Pro source and
  verify the public route.

## Rebuild erased user work

Builder scripts, bulk imports, and direct meta replacement can delete or
recreate documents and erase editor history. Do not use them for existing-site
alignment. Back up the document, then edit only the intended element through
Elementor and verify the saved result before continuing.

## Outer bounds match but design still differs

A forced height or broad CSS override can make section geometry appear correct
while fonts, baselines, padding, gaps, media crops, or responsive behavior still
differ. Compare the inner containers and widgets, remove the parity override,
and express the correction through the exact Elementor controls.

## Correct file, stale frontend

Elementor generated CSS, page caches, browser cache, or a CDN may serve old
assets. Flush only the affected caches and use a bounded cache-busting URL.
When an asset URL is serialized into Elementor data, replacing the file alone
may not update the stored URL.

## Broken native layout

- Elementor container children can default to full width and stack a row.
- Base grid rules with `!important` can defeat less-specific mobile rules.
- A native container background can be erased by later CSS shorthand.
- Lazy background optimization can suppress images before its JS state changes.

Measure the actual container/widget, not only the surrounding section.

## Misplaced decorative icons

Elementor can force container `::before` positioning. A pseudo intended as a
flex/grid item then jumps to a corner or the wrong RTL side. Inspect computed
position and restore static flow only for the affected class.

Accordion icons may retain floats or intrinsic dimensions that turn a circle
into an ellipse. Remove the float and set both outer and inner dimensions with
sufficient specificity.

## Form succeeds but does not store

An explicit `submit_actions` value can omit Elementor Pro’s database action.
Read registered action names from the installed version, submit disposable data,
confirm both submission rows and email, then delete test data.

## Wrong language content

Template translations may be unlinked, Loop queries may not be language-aware,
or language-plugin sync can copy translated meta/taxonomies over the source
language. Inspect settings and mappings before reseeding. Change sync settings
and write translated data in separate requests if settings are request-cached.

## Blank SVG

SVG loaded through `<img>` must be valid XML. Escape characters such as `&` in
attributes. Check `naturalWidth`, response status, and XML parsing rather than
assuming an image cache problem.
