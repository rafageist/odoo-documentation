<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/hr_timesheet_attendance_report_view.xml

- Module: [[docs/Community Addons/hr_timesheet_attendance/hr_timesheet_attendance|hr_timesheet_attendance]]
- Scope: Community Addons
- Source file: `report/hr_timesheet_attendance_report_view.xml`
- Views: 3
- Actions: 3
- Menus: 1
- Rules: 0

## View records

### `hr_timesheet_attendance_report_view_graph`
- Name: hr.timesheet.attendance.report.view.graph
- Model: `hr.timesheet.attendance.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `date`, `total_difference`
- XPath or positional patches: 0

### `view_hr_timesheet_attendance_report_pivot`
- Name: HR timesheet attendance report: Pivot
- Model: `hr.timesheet.attendance.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 7
- Sample fields: `attendance_cost`, `cost_difference`, `date`, `timesheets_cost`, `total_attendance`, `total_difference`, `total_timesheet`
- XPath or positional patches: 0

### `view_hr_timesheet_attendance_report_search`
- Name: Search for HR timesheet attendance report
- Model: `hr.timesheet.attendance.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `employee_id`
- XPath or positional patches: 0

## Actions

- `action_hr_timesheet_attendance_report_graph`: `view`
- `action_hr_timesheet_attendance_report_pivot`: `view`
- `action_hr_timesheet_attendance_report`: `act_window` Timesheets / Attendance Analysis

## Menus

- `menu_hr_timesheet_attendance_report`: Timesheets / Attendance Analysis

## Navigation

- **Parent:** [[docs/Community Addons/hr_timesheet_attendance/Views]]

<!-- GENERATED:VIEWFILE -->
