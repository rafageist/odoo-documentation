<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_leave_views.xml

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Source file: `views/hr_leave_views.xml`
- Views: 21
- Actions: 20
- Menus: 0
- Rules: 0

## View records

### `view_holiday_list`
- Name: hr.holidays.report_list
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `date_from`, `date_to`, `employee_id`, `name`, `number_of_days`, `state`
- XPath or positional patches: 0

### `view_holiday_graph`
- Name: hr.holidays.report_graph
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 6
- Sample fields: `color`, `employee_id`, `number_of_days`, `number_of_hours`, `request_hour_from`, `request_hour_to`
- XPath or positional patches: 0

### `view_holiday_pivot`
- Name: hr.holidays.report_pivot
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 6
- Sample fields: `color`, `date_from`, `employee_id`, `number_of_days`, `request_hour_from`, `request_hour_to`
- XPath or positional patches: 0

### `hr_leave_view_kanban_my`
- Name: hr.leave.view.kanban.my
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_view_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `hr_leave_view_search_report`
- Name: hr.holidays.view.search.report
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `view_hr_holidays_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `hr_leave_view_search_manager`
- Name: hr.holidays.view.search.manager
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `view_hr_holidays_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `department_id`, `employee_id`
- XPath or positional patches: 2

### `hr_leave_view_search_my`
- Name: hr.holidays.view.search.my
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `view_hr_holidays_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 6

### `hr_leave_view_tree_my`
- Name: hr.holidays.view.list
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `hr_leave_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 4

### `hr_leave_view_tree`
- Name: hr.holidays.view.list
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `active_employee`, `activity_exception_decoration`, `company_id`, `date_from`, `date_to`, `department_id`, `duration_display`, `employee_id`, `holiday_status_id`, `message_needaction`, and 3 more
- Buttons: `%(hr_holidays.action_hr_leave_generate_multi_wizard)d`, `action_approve`, `action_refuse`
- XPath or positional patches: 0

### `hr_leave_view_calendar`
- Name: hr.leave.view.calendar
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 6
- Sample fields: `employee_id`, `holiday_status_id`, `is_hatched`, `is_striked`, `name`, `state`
- XPath or positional patches: 0

### `hr_leave_view_form_manager`
- Name: hr.leave.view.form.manager
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `hr_leave_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `company_id`, `department_id`, `employee_id`
- XPath or positional patches: 2

### `hr_leave_employee_view_dashboard`
- Name: hr.leave.view.dashboard
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 5
- Sample fields: `display_name`, `holiday_status_id`, `is_hatched`, `is_striked`, `state`
- XPath or positional patches: 0

### `hr_leave_view_dashboard`
- Name: hr.leave.view.dashboard
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 5
- Sample fields: `display_name`, `holiday_status_id`, `is_hatched`, `is_striked`, `state`
- XPath or positional patches: 0

### `hr_leave_view_form_dashboard_manager_new_time_off`
- Name: hr.leave.view.form.dashboard.new.time.off
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_view_form_dashboard_new_time_off`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `holiday_status_id`, `user_id`
- XPath or positional patches: 1

### `hr_leave_view_form_dashboard_new_time_off`
- Name: hr.leave.view.form.dashboard.new.time.off
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_view_form_dashboard`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 4

### `hr_leave_view_form_dashboard`
- Name: hr.leave.view.form.dashboard
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_view_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `employee_id`, `holiday_status_id`
- XPath or positional patches: 4

### `hr_leave_view_form`
- Name: hr.leave.view.form
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `dashboard_warning_message`, `date_from`, `date_to`, `display_name`, `duration_display`, `employee_id`, `holiday_status_id`, `leave_type_increases_duration`, `name`, `request_date_from`, and 9 more
- Buttons: `action_approve`, `action_back_to_approval`, `action_cancel`, `action_refuse`
- XPath or positional patches: 0

### `hr_leave_view_activity`
- Name: hr.leave.view.activity
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 6
- Sample fields: `date_from`, `date_to`, `employee_id`, `holiday_status_id`, `name`, `number_of_days`
- XPath or positional patches: 0

### `hr_leave_view_kanban`
- Name: hr.leave.view.kanban
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 20
- Sample fields: `can_approve`, `can_refuse`, `can_validate`, `duration_display`, `employee_id`, `holiday_status_id`, `holiday_status_requires_allocation`, `leave_type_request_unit`, `max_leaves`, `request_date_from`, and 10 more
- Buttons: `%(hr_holidays.action_hr_leave_generate_multi_wizard)d`, `action_approve`, `action_documents`, `action_refuse`
- XPath or positional patches: 0

### `view_hr_holidays_filter`
- Name: hr.holidays.filter
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `activity_type_id`, `activity_user_id`, `department_id`, `employee_id`, `holiday_status_id`, `name`, `state`
- XPath or positional patches: 0

### `view_evaluation_report_graph`
- Name: hr.holidays.graph
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `date_from`, `employee_id`, `holiday_status_id`, `number_of_days`
- XPath or positional patches: 0

## Actions

- `action_window_leave_graph`: `view`
- `action_window_leave_list`: `view`
- `action_window_leave_pivot`: `view`
- `action_hr_available_holidays_report`: `act_window` Time Off by Employee
- `action_view_activity_manager_approve`: `view`
- `action_view_calendar_manager_approve`: `view`
- `action_view_form_manager_approve`: `view`
- `action_view_tree_manager_approve`: `view`
- `action_view_kanban_manager_approve`: `view`
- `hr_leave_action_holiday_allocation_id`: `act_window` Time Off
- `hr_leave_action_action_approve_department`: `act_window` All Time Off
- `hr_leave_action_my_view_form`: `view`
- `hr_leave_action_my_view_tree`: `view`
- `hr_leave_action_my`: `act_window` My Time Off
- `hr_leave_action_my_request_view_form`: `view`
- `hr_leave_action_my_request`: `act_window` Time Off Request
- `hr_leave_action_new_request_view_form`: `view`
- `hr_leave_action_new_request_view_tree`: `view`
- `hr_leave_action_new_request_view_calendar`: `view`
- `hr_leave_action_new_request`: `act_window` Dashboard

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Views]]

<!-- GENERATED:VIEWFILE -->
