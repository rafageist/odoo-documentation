<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_timesheet_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_timesheet/helpdesk_timesheet|helpdesk_timesheet]]
- Scope: Enterprise Addons
- Source file: `views/hr_timesheet_views.xml`
- Views: 14
- Actions: 7
- Menus: 0
- Rules: 0

## View records

### `view_calendar_account_analytic_line_multi_create`
- Name: account.analytic.line.calendar.multi_create
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_calendar_account_analytic_line_multi_create`
- Root tag: `field`
- Field references: 2
- Sample fields: `helpdesk_ticket_id`, `task_id`
- XPath or positional patches: 0

### `view_calendar_account_analytic_line`
- Name: account.analytic.line.calendar
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_calendar_account_analytic_line`
- Root tag: `field`
- Field references: 2
- Sample fields: `helpdesk_ticket_id`, `task_id`
- XPath or positional patches: 0

### `hr_timesheet_line_search_helpdesk`
- Name: account.analytic.search
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet_line_search_inherit_helpdesk_timesheet`
- Root tag: `field`
- Field references: 1
- Sample fields: `task_id`
- XPath or positional patches: 2

### `view_kanban_account_analytic_line_helpdesk`
- Name: account.analytic.line.kanban.helpdesk
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet_line_kanban_inherit_helpdesk_timesheet`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `task_id`
- XPath or positional patches: 2

### `hr_timesheet_line_tree_helpdesk`
- Name: account.analytic.line.list.helpdesk
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet_line_tree_inherit_helpdesk_timesheet`
- Root tag: `field`
- Field references: 4
- Sample fields: `helpdesk_ticket_id`, `project_id`, `task_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheet_view_grid_by_employee_ticket`
- Name: sale_timesheet_enterprise.account.analytic.line.grid.employee
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `timesheet_grid.timesheet_view_grid_by_employee_editable_manager`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `helpdesk_ticket_id`
- XPath or positional patches: 2

### `timesheet_view_form_helpdesk_grid`
- Name: account.analytic.line.form.helpdesk.grid
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `helpdesk_timesheet.timesheet_view_form_helpdesk`
- Root tag: `header`
- Field references: 0
- XPath or positional patches: 1

### `timesheet_view_form_helpdesk`
- Name: account.analytic.line.form.helpdesk
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `helpdesk_timesheet.timesheet_view_form_inherit`
- Root tag: `field`
- Field references: 1
- Sample fields: `unit_amount`
- XPath or positional patches: 0

### `timesheet_view_form_inherit`
- Name: account.analytic.line.form.inherit
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `display_task`, `helpdesk_ticket_id`
- XPath or positional patches: 2

### `hr_timesheet_line_search_inherit_helpdesk_timesheet`
- Name: account.analytic.line.search.inherit.helpdesk.timesheet
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `helpdesk_ticket_id`
- XPath or positional patches: 2

### `hr_timesheet_line_kanban_inherit_helpdesk_timesheet`
- Name: account.analytic.line.kanban.inherit.helpdesk.timesheet
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_kanban_account_analytic_line`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `has_helpdesk_team`, `helpdesk_ticket_id`
- XPath or positional patches: 2

### `hr_timesheet_line_tree_inherit_helpdesk_timesheet`
- Name: account.analytic.line.list.inherit.helpdesk.timesheet
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheet_view_tree_user`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `hr_timesheet_line_tree_my_inherit_helpdesk_timesheet`
- Name: account.analytic.line.list.inherit.helpdesk.timesheet
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `has_helpdesk_team`, `helpdesk_ticket_id`
- XPath or positional patches: 2

### `timesheet_view_grid_by_my_timesheet`
- Name: account.analytic.line.grid.project
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `timesheet_grid.timesheet_view_grid`
- Root tag: `field`
- Field references: 2
- Sample fields: `helpdesk_ticket_id`, `task_id`
- XPath or positional patches: 0

## Actions

- `act_hr_timesheet_line_helpdesk_graph`: `view`
- `act_hr_timesheet_line_helpdesk_pivot`: `view`
- `act_hr_timesheet_line_helpdesk_kanban`: `view`
- `act_hr_timesheet_line_helpdesk_grid`: `view`
- `act_hr_timesheet_line_helpdesk_form`: `view`
- `act_hr_timesheet_line_helpdesk_tree`: `view`
- `act_hr_timesheet_line_helpdesk`: `act_window` Timesheets

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
