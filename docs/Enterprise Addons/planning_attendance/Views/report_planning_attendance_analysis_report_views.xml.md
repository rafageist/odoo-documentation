<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/planning_attendance_analysis_report_views.xml

- Module: [[docs/Enterprise Addons/planning_attendance/planning_attendance|planning_attendance]]
- Scope: Enterprise Addons
- Source file: `report/planning_attendance_analysis_report_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `planning_attendance_analysis_report_view_search`
- Name: planning.attendance.analysis.report.search
- Model: `planning.attendance.analysis.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `department_id`, `employee_id`
- XPath or positional patches: 0

### `planning_attendance_analysis_report_view_graph`
- Name: planning.attendance.analysis.report.graph
- Model: `planning.attendance.analysis.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 7
- Sample fields: `cost_difference`, `effective_costs`, `effective_hours`, `entry_date`, `planned_costs`, `planned_hours`, `time_difference`
- XPath or positional patches: 0

### `planning_attendance_analysis_report_view_pivot`
- Name: planning.attendance.analysis.report.pivot
- Model: `planning.attendance.analysis.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 7
- Sample fields: `cost_difference`, `effective_costs`, `effective_hours`, `entry_date`, `planned_costs`, `planned_hours`, `time_difference`
- XPath or positional patches: 0

## Actions

- `planning_attendance_analysis_report_action`: `act_window` Planning / Attendance Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/planning_attendance/Views]]

<!-- GENERATED:VIEWFILE -->
