---
tags: [odoo, enterprise, generated, views]
---

# views/spreadsheet_views.xml

- Module: [[docs/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]]
- Scope: Enterprise Addons
- Source file: `views/spreadsheet_views.xml`
- Views: 2
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `spreadsheet_revision_view_tree`
- Name: spreadsheet.revision list view
- Model: `spreadsheet.revision`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `create_date`, `name`, `res_id`, `res_model`, `revision_uuid`
- XPath or positional patches: 0

### `spreadsheet_revision_view_search`
- Name: spreadsheet.revision search view
- Model: `spreadsheet.revision`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `res_id`, `res_model`
- XPath or positional patches: 0

## Actions

- `spreadsheet_revision_action`: `act_window` Revisions

## Menus

- `menu_technical_spreadsheet_revision`: Revisions
- `menu_technical_spreadsheet`: Spreadsheet

## Navigation

- **Parent:** [[docs/Enterprise Addons/spreadsheet_edition/Views]]

