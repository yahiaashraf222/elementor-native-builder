# Workflow

## 1. Establish the contract

Inventory:

- reference files, routes, sections, states, and assets;
- languages and RTL/LTR behavior;
- required viewport widths;
- editable fields, repeated entities, filters, forms, and single/archive views;
- performance, accessibility, and deployment constraints.

Create a page matrix. A page is not complete until every expected section and
language exists and the reference comparison is recorded.

## 2. Inspect the live stack

Read the actual versions and code:

- WordPress, PHP, Elementor, Elementor Pro, active parent and child theme;
- active Elementor features such as Containers, Nested Elements, Atomic
  Widgets, lazy backgrounds, and optimized DOM;
- Theme Builder locations and template conditions;
- CPTs, taxonomies, meta, dynamic tags, language mappings, and rewrite rules;
- caches, CDN behavior, SMTP, and deployment tooling.

If installed behavior differs from documentation, preserve evidence and design
for the installed version. Do not silently upgrade dependencies.

## 3. Choose an architecture

For an existing Elementor site, use the native editor/model for every change.
Do not use builder scripts, bulk imports, direct meta writes, or generated JSON
replacement. For a new multilingual site, establish reusable native templates,
Loop Items, and Site Settings manually through the editor before scaling.

Map:

- site globals and tokens;
- header/footer and Theme Builder templates;
- page containers and native widgets;
- Loop Item templates and queries;
- CPT/meta/taxonomy ownership;
- forms and submission actions;
- custom widgets/tags required only for gaps.

## 4. Build in vertical slices

Prove one complete slice before scaling:

1. global styles and one header/footer language;
2. one representative page or section;
3. one Loop Item and Loop Grid;
4. one dynamic single template;
5. one form;
6. responsive and translated variants.

At each slice:

1. capture the matching reference and live component in Playwright;
2. wait for `document.fonts.ready` and measure the outer section plus its
   relevant inner containers and widgets;
3. open the exact Elementor page/template and select it in Navigator;
4. change native controls for one section or template only;
5. save, reload the editor, and inspect the saved responsive data;
6. reload the frontend and verify desktop, tablet, and mobile before continuing.

Do not accept a matching outer rectangle when inner typography, gaps, padding,
alignment, media crops, or controls still differ.

## 5. Preserve rebuildability

- Name templates and Navigator containers clearly.
- Record document IDs, template types, language links, and conditions.
- Keep reusable content in WordPress and reusable layout in native templates.
- Use Site Settings for shared visual tokens.
- Refuse a bulk rebuild when manual edits exist. Restore or edit the affected
  document section-by-section instead.

## Native section operations

- **Edit:** select the exact container/widget in Navigator, change its native
  content/style/advanced controls, set each required responsive value, and save.
- **Add:** insert a native container/widget in the intended parent, configure
  layout and responsive controls, name it, then save and verify its new ID.
- **Duplicate:** use Elementor Duplicate in Navigator. Confirm Elementor created
  unique IDs, then update content, controls, and accessible names before saving.
- **Move:** drag the selected element in Navigator to the intended parent/order.
  Save, reopen, and confirm both Navigator placement and JSON parent/order.
- **Delete:** export/back up the document, delete only the selected element in
  Navigator, save, and verify no shared template or responsive sibling changed.

## 6. Verify and hand off

Use the full checklist in `verification.md`. Report:

- modified code and generated documents;
- native/custom/exception widget counts;
- routes and viewports checked;
- language and interaction results;
- rollback locations and restore commands;
- known limitations, if any.
