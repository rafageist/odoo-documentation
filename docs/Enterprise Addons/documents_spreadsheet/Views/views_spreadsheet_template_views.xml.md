---
tags: [odoo, enterprise, generated, views]
---

# views/spreadsheet_template_views.xml

- Module: [[docs/Enterprise Addons/documents_spreadsheet/documents_spreadsheet|documents_spreadsheet]]
- Scope: Enterprise Addons
- Source file: `views/spreadsheet_template_views.xml`
- Views: 4
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `spreadsheet_contributor_view_form`
- Name: spreadsheet.revision form view
- Model: `spreadsheet.revision`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `commands`, `create_date`, `res_id`, `res_model`, `revision_uuid`
- XPath or positional patches: 0

### `spreadsheet_template_view_search`
- Name: spreadsheet search view
- Model: `spreadsheet.template`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `spreadsheet_template_view_tree`
- Name: spreadsheet.template
- Model: `spreadsheet.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `create_date`, `create_uid`, `file_name`, `name`, `sequence`, `spreadsheet_binary_data`, `thumbnail`
- Buttons: `action_create_spreadsheet`, `action_edit_template`, `copy`
- XPath or positional patches: 0

### `spreadsheet_contributor_view_tree`
- Name: spreadsheet.contributor
- Model: `spreadsheet.contributor`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `document_id`, `user_id`
- XPath or positional patches: 0

## Actions

- `spreadsheet_template_action`: `act_window` Spreadsheet Templates
- `spreadsheet_contributor_action`: `act_window` Contributors

## Menus

- `menu_technical_spreadsheet_contributor`: Contributors
- `menu_technical_spreadsheet_template`: Spreadsheet Templates

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents_spreadsheet/Views]]

