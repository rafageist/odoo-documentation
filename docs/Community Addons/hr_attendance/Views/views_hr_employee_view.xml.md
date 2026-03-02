<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_employee_view.xml

- Module: [[docs/Community Addons/hr_attendance/hr_attendance|hr_attendance]]
- Scope: Community Addons
- Source file: `views/hr_employee_view.xml`
- Views: 6
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_attendance_employee_simple_form_view`
- Name: hr.attendance.form
- Model: `hr.attendance`
- Type: inferred from arch
- Inherits: `hr_attendance.hr_attendance_view_form`
- Root tag: `field`
- Field references: 4
- Sample fields: `check_in`, `check_out`, `overtime_status`, `validated_overtime_hours`
- Buttons: `action_approve_overtime`, `action_refuse_overtime`
- XPath or positional patches: 3

### `hr_attendance_employee_simple_tree_view`
- Name: hr.attendance.list
- Model: `hr.attendance`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `check_in`, `check_out`, `overtime_status`, `validated_overtime_hours`, `worked_hours`
- XPath or positional patches: 0

### `view_employee_tree_inherit_leave`
- Name: hr.employee.list.leave
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `attendance_manager_id`
- XPath or positional patches: 1

### `hr_employees_view_kanban`
- Name: hr.employee.kanban
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `attendance_state`, `avatar_128`, `job_id`, `name`, `work_location_id`
- XPath or positional patches: 0

### `view_employee_form_inherit_hr_attendance`
- Name: hr.employee
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `button`
- Field references: 5
- Sample fields: `attendance_manager_id`, `attendance_state`, `hours_last_month`, `hours_last_month_overtime`, `ruleset_id`
- Buttons: `action_open_last_month_attendances`, `action_open_versions`, `open_barcode_scanner`
- XPath or positional patches: 4

### `hr_employee_search_view`
- Name: hr.employee.search.view
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `hr_employee_attendance_action_kanban`: `act_window` Employees

## Navigation

- **Parent:** [[docs/Community Addons/hr_attendance/Views]]

<!-- GENERATED:VIEWFILE -->
