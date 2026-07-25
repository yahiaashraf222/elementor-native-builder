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

For a small existing page, editor changes may be safest. For a multilingual,
multi-page reference build, use repeatable builder scripts that emit supported
Elementor documents and preserve a clear rebuild boundary.

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

At each slice, verify structure, frontend render, editor visibility, and
rollback before multiplying the pattern.

## 5. Preserve rebuildability

- Tag or otherwise identify generated templates.
- Record source script, output document IDs, language links, and conditions.
- Keep content dictionaries separate from layout helpers.
- Keep stable visual CSS in the child theme.
- Refuse a destructive rebuild when manual edits exist unless the user approves
  the replacement and a restorable snapshot exists.

## 6. Verify and hand off

Use the full checklist in `verification.md`. Report:

- modified code and generated documents;
- native/custom/exception widget counts;
- routes and viewports checked;
- language and interaction results;
- rollback locations and restore commands;
- known limitations, if any.
