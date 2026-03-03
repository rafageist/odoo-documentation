---
tags: [odoo, community, generated, views]
---

# views/spreadsheet_dashboard_views.xml

- Module: [[docs/Community Addons/spreadsheet_dashboard/spreadsheet_dashboard|spreadsheet_dashboard]]
- Scope: Community Addons
- Source file: `views/spreadsheet_dashboard_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `spreadsheet_dashboard_view_kanban`
- Name: spreadsheet.dashboard.kanban
- Model: `spreadsheet.dashboard`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `spreadsheet_dashboard_view_form`
- Name: spreadsheet.dashboard.view.form
- Model: `spreadsheet.dashboard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `company_ids`, `dashboard_group_id`, `group_ids`, `name`, `spreadsheet_binary_data`
- XPath or positional patches: 0

### `spreadsheet_dashboard_container_view_form`
- Name: spreadsheet.dashboard.group.view.form
- Model: `spreadsheet.dashboard.group`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `dashboard_ids`, `name`
- XPath or positional patches: 0

### `spreadsheet_dashboard_container_view_list`
- Name: spreadsheet.dashboard.group.view.list
- Model: `spreadsheet.dashboard.group`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `name`, `sequence`
- XPath or positional patches: 0

### `spreadsheet_dashboard_view_list`
- Name: spreadsheet.dashboard.view.list
- Model: `spreadsheet.dashboard`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_ids`, `dashboard_group_id`, `group_ids`, `is_published`, `name`, `sequence`, `spreadsheet_binary_data`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/spreadsheet_dashboard/Views]]

