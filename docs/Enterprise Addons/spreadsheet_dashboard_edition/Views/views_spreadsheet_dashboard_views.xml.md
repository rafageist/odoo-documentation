---
tags: [odoo, enterprise, generated, views]
---

# views/spreadsheet_dashboard_views.xml

- Module: [[docs/Enterprise Addons/spreadsheet_dashboard_edition/spreadsheet_dashboard_edition|spreadsheet_dashboard_edition]]
- Scope: Enterprise Addons
- Source file: `views/spreadsheet_dashboard_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `spreadsheet_dashboard_creation_dialog_view_form`
- Name: spreadsheet.dashboard.quick.create.form
- Model: `spreadsheet.dashboard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `dashboard_group_id`, `group_ids`, `name`
- XPath or positional patches: 0

### `spreadsheet_dashboard_kanban_view_inherit`
- Name: spreadsheet.dashboard.kanban.inherit
- Model: `spreadsheet.dashboard`
- Type: inferred from arch
- Inherits: `spreadsheet_dashboard.spreadsheet_dashboard_view_kanban`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_edit_dashboard`
- XPath or positional patches: 1

### `spreadsheet_dashboard_view_list`
- Name: spreadsheet.dashboard.list.view
- Model: `spreadsheet.dashboard`
- Type: inferred from arch
- Inherits: `spreadsheet_dashboard.spreadsheet_dashboard_view_list`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `spreadsheet_file_name`
- Buttons: `action_edit_dashboard`
- XPath or positional patches: 2

## Actions

- `action_spreadsheet_dashboard_edit`: `server` Edit

## Navigation

- **Parent:** [[docs/Enterprise Addons/spreadsheet_dashboard_edition/Views]]

