<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/hr_leave_reports.xml

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Source file: `report/hr_leave_reports.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `hr_leave_report_pivot`
- Name: report.hr.holidays.report.leave_all.pivot
- Model: `hr.leave.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `employee_id`, `number_of_days`, `number_of_hours`
- XPath or positional patches: 0

### `hr_leave_report_graph`
- Name: report.hr.holidays.report.leave_all.graph
- Model: `hr.leave.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `employee_id`, `leave_type`, `number_of_days`, `number_of_hours`
- XPath or positional patches: 0

### `hr_leave_report_tree`
- Name: report.hr.holidays.report.leave_all.list
- Model: `hr.leave.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `date_from`, `date_to`, `employee_id`, `leave_type`, `name`, `number_of_days`, `number_of_hours`, `state`
- XPath or positional patches: 0

### `view_hr_holidays_filter_report`
- Name: hr.holidays.filter
- Model: `hr.leave.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `department_id`, `employee_id`, `holiday_status_id`, `name`
- XPath or positional patches: 0

## Actions

- `hr_leave_report_action`: `act_window` Time Off Analysis
- `action_hr_leave_report`: `act_window` Time Off by Type

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Views]]

<!-- GENERATED:VIEWFILE -->
