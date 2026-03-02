<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_leave_allocation_views.xml

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Source file: `views/hr_leave_allocation_views.xml`
- Views: 11
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `hr_leave_allocation_view_activity`
- Name: hr.leave.allocation.view.activity
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 3
- Sample fields: `employee_id`, `holiday_status_id`, `number_of_days`
- XPath or positional patches: 0

### `hr_leave_allocation_view_kanban`
- Name: hr.leave.allocation.view.kanban
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 11
- Sample fields: `allocation_type`, `can_approve`, `can_refuse`, `can_validate`, `duration_display`, `employee_id`, `holiday_status_id`, `max_leaves`, `state`, `virtual_remaining_leaves`, and 1 more
- Buttons: `%(hr_holidays.action_hr_leave_allocation_generate_multi_wizard)d`, `action_approve`, `action_refuse`
- XPath or positional patches: 0

### `hr_leave_allocation_view_search_manager`
- Name: hr.leave.allocation.view.search.my
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Inherits: `view_hr_leave_allocation_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `hr_leave_allocation_view_search_my`
- Name: hr.leave.allocation.view.search.my
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Inherits: `view_hr_leave_allocation_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 6

### `hr_leave_allocation_view_tree_my`
- Name: hr.leave.allocation.view.list.my
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Inherits: `hr_leave_allocation_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `hr_leave_allocation_view_tree`
- Name: hr.leave.allocation.view.list
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Root tag: `list`
- Field references: 14
- Sample fields: `accrual_plan_id`, `active_employee`, `activity_exception_decoration`, `allocation_type`, `date_from`, `date_to`, `department_id`, `duration_display`, `employee_id`, `holiday_status_id`, and 4 more
- Buttons: `%(hr_holidays.action_hr_leave_allocation_generate_multi_wizard)d`, `action_approve`, `action_refuse`
- XPath or positional patches: 0

### `hr_leave_allocation_view_form_manager_dashboard`
- Name: hr.leave.allocation.view.form.manager.dashboard
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_allocation_view_form_manager`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `hr_leave_allocation_view_form_dashboard`
- Name: hr.leave.view.form.dashboard
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_allocation_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 11

### `hr_leave_allocation_view_form_manager`
- Name: hr.leave.allocation.view.form.manager
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_allocation_view_form`
- Root tag: `div`
- Field references: 5
- Sample fields: `allocation_type`, `date_from`, `date_to`, `employee_id`, `name`
- XPath or positional patches: 4

### `hr_leave_allocation_view_form`
- Name: hr.leave.allocation.view.form
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `accrual_plan_id`, `allocation_type`, `already_accrued`, `can_approve`, `carried_over_days_expiration_date`, `date_from`, `date_to`, `employee_id`, `expiring_carryover_days`, `holiday_status_id`, and 11 more
- Buttons: `action_approve`, `action_refuse`
- XPath or positional patches: 0

### `view_hr_leave_allocation_filter`
- Name: hr.holidays.filter_allocations
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Root tag: `search`
- Field references: 9
- Sample fields: `accrual_plan_id`, `activity_type_id`, `activity_user_id`, `allocation_type`, `department_id`, `employee_id`, `holiday_status_id`, `name`, `state`
- XPath or positional patches: 0

## Actions

- `hr_leave_allocation_action_approve_department`: `act_window` Allocations
- `hr_leave_allocation_action_form`: `act_window` New allocation
- `hr_leave_allocation_action_all`: `act_window` All Allocations
- `hr_leave_allocation_action_my_view_form`: `view`
- `hr_leave_allocation_action_my_view_tree`: `view`
- `hr_leave_allocation_action_my`: `act_window` My Allocations

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Views]]

<!-- GENERATED:VIEWFILE -->
