<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/lunch_cashmove_report_views.xml

- Module: [[docs/Community Addons/lunch/lunch|lunch]]
- Scope: Community Addons
- Source file: `report/lunch_cashmove_report_views.xml`
- Views: 6
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_lunch_cashmove_report_kanban`
- Name: lunch.cashmove.report.kanban
- Model: `lunch.cashmove.report`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `amount`, `currency_id`, `date`, `description`, `user_id`
- XPath or positional patches: 0

### `lunch_cashmove_report_view_form`
- Name: lunch.cashmove.report.form
- Model: `lunch.cashmove.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `amount`, `currency_id`, `date`, `description`, `user_id`
- XPath or positional patches: 0

### `lunch_cashmove_report_view_tree_2`
- Name: lunch.cashmove.report.list
- Model: `lunch.cashmove.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `amount`, `currency_id`, `date`, `description`
- XPath or positional patches: 0

### `lunch_cashmove_report_view_tree`
- Name: lunch.cashmove.report.list
- Model: `lunch.cashmove.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `amount`, `currency_id`, `date`, `description`, `user_id`
- XPath or positional patches: 0

### `lunch_cashmove_report_view_search_2`
- Name: lunch.cashmove.report.search
- Model: `lunch.cashmove.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `description`, `user_id`
- XPath or positional patches: 0

### `lunch_cashmove_report_view_search`
- Name: lunch.cashmove.report.search
- Model: `lunch.cashmove.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `description`, `user_id`
- XPath or positional patches: 0

## Actions

- `lunch_cashmove_report_action_control_accounts`: `act_window` Control Accounts
- `lunch_cashmove_report_action_account`: `act_window` My Account

## Navigation

- **Parent:** [[docs/Community Addons/lunch/Views]]

<!-- GENERATED:VIEWFILE -->
