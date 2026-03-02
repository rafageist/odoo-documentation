<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_attendance_view.xml

- Module: [[docs/Community Addons/hr_attendance/hr_attendance|hr_attendance]]
- Scope: Community Addons
- Source file: `views/hr_attendance_view.xml`
- Views: 8
- Actions: 7
- Menus: 10
- Rules: 0

## View records

### `view_attendance_tree_management`
- Name: hr.attendance.list
- Model: `hr.attendance`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `check_in`, `check_out`, `employee_id`, `overtime_hours`, `validated_overtime_hours`, `worked_hours`
- Buttons: `action_approve_overtime`, `action_refuse_overtime`
- XPath or positional patches: 0

### `hr_attendance_management_view_filter`
- Name: hr_attendance_management_view_filter
- Model: `hr.attendance`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `department_id`, `employee_id`
- XPath or positional patches: 0

### `hr_attendance_view_filter`
- Name: hr_attendance_view_filter
- Model: `hr.attendance`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `check_in`, `department_id`, `employee_id`
- XPath or positional patches: 0

### `hr_attendance_view_pivot`
- Name: hr.attendance.pivot
- Model: `hr.attendance`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 6
- Sample fields: `check_in`, `employee_id`, `expected_hours`, `overtime_hours`, `validated_overtime_hours`, `worked_hours`
- XPath or positional patches: 0

### `hr_attendance_view_graph`
- Name: hr.attendance.graph
- Model: `hr.attendance`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `check_in`, `employee_id`, `overtime_hours`, `worked_hours`
- XPath or positional patches: 0

### `hr_attendance_view_form`
- Name: hr.attendance.form
- Model: `hr.attendance`
- Type: inferred from arch
- Root tag: `form`
- Field references: 25
- Sample fields: `amount_rate`, `check_in`, `check_out`, `duration`, `employee_id`, `in_browser`, `in_ip_address`, `in_latitude`, `in_location`, `in_longitude`, and 15 more
- Buttons: `action_approve`, `action_approve_overtime`, `action_in_attendance_maps`, `action_out_attendance_maps`, `action_refuse`, `action_refuse_overtime`
- XPath or positional patches: 0

### `view_hr_attendance_kanban`
- Name: hr.attendance.kanban
- Model: `hr.attendance`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `check_in`, `check_out`, `employee_id`
- XPath or positional patches: 0

### `view_attendance_tree`
- Name: hr.attendance.list
- Model: `hr.attendance`
- Type: inferred from arch
- Root tag: `list`
- Field references: 19
- Sample fields: `check_in`, `check_out`, `color`, `create_uid`, `employee_id`, `in_latitude`, `in_location`, `in_longitude`, `in_mode`, `out_latitude`, and 9 more
- Buttons: `action_approve_overtime`, `action_refuse_overtime`
- XPath or positional patches: 0

## Actions

- `open_kiosk_url`: `server` Open Kiosk Url
- `hr_attendance_action_greeting_message`: `client` Message
- `hr_attendance_management_action`: `act_window` Management
- `hr_attendance_reporting`: `act_window` Attendances
- `hr_attendance_action`: `act_window` Attendances
- `action_load_demo_data`: `server` Load demo data
- `action_try_kiosk`: `server` Try kiosk

## Menus

- `menu_hr_attendance_onboarding`: Onboarding
- `menu_hr_attendance_configuration`: Configuration
- `menu_hr_attendance_view_attendances_management`: Management
- `menu_hr_attendance_employee`: Employees
- `menu_hr_attendance_view_dashboard`: Dashboard
- `menu_hr_attendance_overview`: Overview
- `menu_hr_attendance_attendance_reporting`: Attendances
- `menu_hr_attendance_reporting`: Reporting
- `menu_action_open_form`: Kiosk Mode
- `menu_hr_attendance_root`: Attendances

## Navigation

- **Parent:** [[docs/Community Addons/hr_attendance/Views]]

<!-- GENERATED:VIEWFILE -->
