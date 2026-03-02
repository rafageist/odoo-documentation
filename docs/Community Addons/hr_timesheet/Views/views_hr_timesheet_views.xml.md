<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_timesheet_views.xml

- Module: [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]
- Scope: Community Addons
- Source file: `views/hr_timesheet_views.xml`
- Views: 20
- Actions: 23
- Menus: 0
- Rules: 0

## View records

### `view_kanban_account_analytic_line_portal_user`
- Name: portal.account.analytic.line.kanban
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_kanban_account_analytic_line`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_calendar_account_analytic_line_my_timesheets`
- Name: account.analytic.line.calendar
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_calendar_account_analytic_line`
- Root tag: `calendar`
- Field references: 1
- Sample fields: `employee_id`
- XPath or positional patches: 1

### `view_calendar_account_analytic_line_multi_create`
- Name: account.analytic.line.calendar.multi_create
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `name`, `project_id`, `task_id`, `unit_amount`
- XPath or positional patches: 0

### `view_calendar_account_analytic_line`
- Name: account.analytic.line.calendar
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 4
- Sample fields: `employee_id`, `name`, `project_id`, `task_id`
- XPath or positional patches: 0

### `view_kanban_account_analytic_line`
- Name: account.analytic.line.kanban
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `company_id`, `date`, `employee_id`, `name`, `project_id`, `task_id`, `unit_amount`
- XPath or positional patches: 0

### `hr_timesheet_line_my_timesheet_search`
- Name: view.search.my.timesheet.menu
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet_line_search`
- Root tag: `field`
- Field references: 3
- Sample fields: `department_id`, `employee_id`, `manager_id`
- XPath or positional patches: 4

### `timesheet_view_form_portal_user`
- Name: account.analytic.line.form
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheet_view_form_user`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `hr_timesheet_line_search`
- Name: account.analytic.line.search
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `analytic.view_account_analytic_line_filter`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `department_id`, `employee_id`, `manager_id`, `parent_task_id`, `project_id`, `task_id`
- XPath or positional patches: 4

### `timesheet_view_form_user`
- Name: account.analytic.line.list.with.user
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `employee_id`, `user_id`
- XPath or positional patches: 1

### `hr_timesheet_line_form`
- Name: account.analytic.line.form
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `amount`, `company_id`, `currency_id`, `date`, `name`, `project_id`, `readonly_timesheet`, `task_id`, `unit_amount`
- XPath or positional patches: 0

### `view_hr_timesheet_line_graph_by_employee`
- Name: account.analytic.line.graph.by.employee
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_hr_timesheet_line_graph_all`
- Root tag: `field`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 0

### `view_hr_timesheet_line_by_project`
- Name: account.analytic.line.graph.by.project
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_hr_timesheet_line_graph_all`
- Root tag: `field`
- Field references: 4
- Sample fields: `date`, `employee_id`, `project_id`, `task_id`
- XPath or positional patches: 0

### `view_hr_timesheet_line_graph_all`
- Name: account.analytic.line.graph
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `amount`, `employee_id`, `project_id`, `unit_amount`
- XPath or positional patches: 0

### `view_hr_timesheet_line_graph_my`
- Name: account.analytic.line.graph
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `amount`, `date`, `project_id`, `unit_amount`
- XPath or positional patches: 0

### `view_hr_timesheet_line_graph`
- Name: account.analytic.line.graph
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `amount`, `project_id`, `task_id`, `unit_amount`
- XPath or positional patches: 0

### `view_my_timesheet_line_pivot`
- Name: account.analytic.line.pivot
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `amount`, `date`, `unit_amount`
- XPath or positional patches: 0

### `view_hr_timesheet_line_pivot`
- Name: account.analytic.line.pivot
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `amount`, `date`, `employee_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheet_view_tree_user`
- Name: account.analytic.line.view.list.with.user
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet_line_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `hr_timesheet_line_portal_tree`
- Name: portal.hr_timesheet.account.analytic.line.list
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet_line_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `hr_timesheet_line_tree`
- Name: account.analytic.line.list.hr_timesheet
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `company_id`, `date`, `employee_id`, `name`, `project_id`, `readonly_timesheet`, `task_id`, `unit_amount`, `user_id`
- XPath or positional patches: 0

## Actions

- `act_hr_timesheet_line_by_project_view_form`: `view`
- `act_hr_timesheet_line_by_project_view_graph`: `view`
- `act_hr_timesheet_line_by_project_view_pivot`: `view`
- `act_hr_timesheet_line_by_project_view_kanban`: `view`
- `act_hr_timesheet_line_by_project_view_tree`: `view`
- `act_hr_timesheet_line_by_project`: `act_window` Timesheets
- `timesheet_action_from_employee`: `act_window` Timesheets
- `timesheet_action_view_all_graph`: `view`
- `timesheet_action_view_all_pivot`: `view`
- `timesheet_action_view_all_kanban`: `view`
- `timesheet_action_view_all_calendar`: `view`
- `timesheet_action_view_all_form`: `view`
- `timesheet_action_view_all_tree`: `view`
- `timesheet_action_all`: `act_window` All Timesheets
- `timesheet_action_project`: `act_window` Project's Timesheets
- `timesheet_action_task`: `act_window` Task's Timesheets
- `act_hr_timesheet_line_view_graph`: `view`
- `act_hr_timesheet_line_view_pivot`: `view`
- `act_hr_timesheet_line_view_kanban`: `view`
- `act_hr_timesheet_line_view_calendar`: `view`

## Navigation

- **Parent:** [[docs/Community Addons/hr_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
