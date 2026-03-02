<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_analytic_line_views.xml

- Module: [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]]
- Scope: Enterprise Addons
- Source file: `views/account_analytic_line_views.xml`
- Views: 21
- Actions: 26
- Menus: 0
- Rules: 0

## View records

### `view_calendar_account_analytic_line`
- Name: account.analytic.line.calendar
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_calendar_account_analytic_line`
- Root tag: `calendar`
- Field references: 1
- Sample fields: `is_hatched`
- XPath or positional patches: 1

### `timesheet_grid_pivot_view_all_validate`
- Name: account.analytic.line.pivot.weekly.validate.timesheet_grid
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_hr_timesheet_line_pivot`
- Root tag: `pivot`
- Field references: 0
- XPath or positional patches: 1

### `hr_timesheet_line_inherit_my_timesheet_search`
- Name: view.search.my.timesheet.inherit
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_my_timesheet_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

### `hr_timesheet.hr_timesheet_line_my_timesheet_search`
- Name: unnamed
- Model: not declared
- Type: inferred from arch
- Inherits: `timesheet_view_search`
- Field references: 0
- XPath or positional patches: 0

### `timesheet_view_search`
- Name: account.analytic.search
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `timesheet_view_grid_by_employee_validation_last_period_by_defaut`
- Name: account.analytic.line.grid.employee.validation
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `timesheet_grid.timesheet_view_grid_by_employee_validation`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `timesheet_view_grid_by_employee_validation`
- Name: account.analytic.line.grid.employee.validation
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `timesheet_grid.timesheet_view_grid_by_employee_editable_manager`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_validate_timesheet`
- XPath or positional patches: 1

### `timesheet_view_grid_by_employee_editable_manager`
- Name: account.analytic.line.grid.employee.manager
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `timesheet_grid.timesheet_view_grid_by_employee`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 1

### `timesheet_view_grid_by_employee_readonly`
- Name: account.analytic.line.grid.employee.readonly
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `timesheet_grid.timesheet_view_grid_by_employee`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `timesheet_view_grid_by_employee`
- Name: account.analytic.line.grid.employee
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `grid`
- Field references: 5
- Sample fields: `date`, `employee_id`, `project_id`, `task_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheet_view_grid_by_project`
- Name: account.analytic.line.grid.project
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `grid`
- Field references: 5
- Sample fields: `date`, `employee_id`, `project_id`, `task_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheet_view_grid`
- Name: account.analytic.line.grid.project
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `grid`
- Field references: 5
- Sample fields: `date`, `employee_id`, `project_id`, `task_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheet_view_form_user_grid`
- Name: account.analytic.line.form.user.grid
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheet_view_form_user`
- Root tag: `header`
- Field references: 0
- XPath or positional patches: 1

### `hr_timesheet_line_form_grid`
- Name: account.analytic.line.form.grid
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_form`
- Root tag: `header`
- Field references: 0
- XPath or positional patches: 1

### `timesheet_form_view`
- Name: account.analytic.line.kanban.timesheet_grid
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `timer_start`, `user_can_validate`, `validated`, `validated_status`
- Buttons: `action_invalidate_timesheet`, `action_validate_timesheet`
- XPath or positional patches: 3

### `timesheet_kanban_view`
- Name: account.analytic.line.kanban.timesheet_grid
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `timesheet_grid.view_kanban_account_analytic_line_inherit_timesheet_grid`
- Root tag: `kanban`
- Field references: 6
- Sample fields: `display_timer`, `is_timer_running`, `name`, `readonly_timesheet`, `timer_start`, `unit_amount`
- XPath or positional patches: 6

### `view_kanban_account_analytic_line_inherit_timesheet_grid_validation`
- Name: account.analytic.line.kanban.timesheet_grid.validation.btn
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `timesheet_grid.view_kanban_account_analytic_line_inherit_timesheet_grid`
- Root tag: `kanban`
- Field references: 0
- XPath or positional patches: 1

### `view_kanban_account_analytic_line_inherit_timesheet_grid`
- Name: account.analytic.line.view.kanban.inherit.timesheet.grid
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_kanban_account_analytic_line`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `validated`
- XPath or positional patches: 1

### `timesheet_view_tree_user_inherited`
- Name: account.analytic.line.list.timesheet_grid
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheet_view_tree_user`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `is_timer_running`
- Buttons: `action_validate_timesheet`
- XPath or positional patches: 3

### `timesheet_view_tree_user_grid_inherited`
- Name: account.analytic.line.list.grid.timesheet_grid
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheet_view_tree_user`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `timesheet_view_tree_colored`
- Name: account.analytic.line.list.hr_timesheet
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_tree`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `display_timer`, `is_timer_running`, `timer_start`
- XPath or positional patches: 4

## Actions

- `merge_timesheet_action`: `server` Merge Timesheets
- `invalidate_timesheet_action`: `server` Reset to draft
- `hr_timesheet_to_validate_all_timesheets_action_form`: `view`
- `hr_timesheet_to_validate_all_timesheets_action_kanban`: `view`
- `hr_timesheet_to_validate_all_timesheets_action_calendar`: `view`
- `hr_timesheet_to_validate_all_timesheets_action_tree`: `view`
- `hr_timesheet_to_validate_all_timesheets_action_grid`: `view`
- `hr_timesheet_to_validate_action_pivot`: `view`
- `timesheet_grid_to_validate_all_timesheets_action`: `act_window` Timesheets to Validate
- `hr_timesheet_to_validate_action_form`: `view`
- `hr_timesheet_to_validate_action_kanban`: `view`
- `hr_timesheet_to_validate_action_calendar`: `view`
- `hr_timesheet_to_validate_action_tree`: `view`
- `hr_timesheet_to_validate_action_grid`: `view`
- `timesheet_grid_to_validate_action`: `act_window` Timesheets to Validate
- `hr_timesheet.timesheet_action_view_from_employee_form`: `view`
- `timesheet_action_view_form_employee_grid`: `view`
- `hr_timesheet.timesheet_action_view_all_form`: `view`
- `timesheet_action_view_all_grid`: `view`
- `hr_timesheet.timesheet_action_all`: `act_window` All Timesheets

## Navigation

- **Parent:** [[docs/Enterprise Addons/timesheet_grid/Views]]

<!-- GENERATED:VIEWFILE -->
