<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_leave_attendance_report_views.xml

- Module: [[docs/Community Addons/hr_holidays_attendance/hr_holidays_attendance|hr_holidays_attendance]]
- Scope: Community Addons
- Source file: `views/hr_leave_attendance_report_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `hr_leave_attendance_report_view_search`
- Name: hr.leave.attendance.report.search
- Model: `hr.leave.attendance.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `date`, `employee_id`, `schedule_id`
- XPath or positional patches: 0

### `hr_leave_attendance_report_view_form`
- Name: hr.leave.attendance.report.form
- Model: `hr.leave.attendance.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `attendance_ids`, `check_in`, `check_out`, `date`, `date_from`, `date_to`, `difference_hours`, `duration_display`, `employee_id`, `expected_hours`, and 7 more
- XPath or positional patches: 0

### `hr_leave_attendance_report_view_pivot`
- Name: hr.leave.attendance.report.pivot
- Model: `hr.leave.attendance.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 6
- Sample fields: `date`, `difference_hours`, `employee_id`, `expected_hours`, `leave_hours`, `worked_hours`
- XPath or positional patches: 0

### `hr_leave_attendance_report_view_list`
- Name: hr.leave.attendance.report.list
- Model: `hr.leave.attendance.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `date`, `difference_hours`, `employee_id`, `expected_hours`, `leave_hours`, `leave_type_names`, `schedule_id`, `worked_hours`
- XPath or positional patches: 0

## Actions

- `hr_leave_attendance_report_action`: `act_window` Time Off Ledger

## Menus

- `hr_leave_attendance_report`: Time Off Ledger

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays_attendance/Views]]

<!-- GENERATED:VIEWFILE -->
