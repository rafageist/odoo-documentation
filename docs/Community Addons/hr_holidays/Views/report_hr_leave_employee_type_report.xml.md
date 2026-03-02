<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/hr_leave_employee_type_report.xml

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Source file: `report/hr_leave_employee_type_report.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_leave_employee_type_report`
- Name: hr.leave.employee.type.report.view.pivot
- Model: `hr.leave.employee.type.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `employee_id`, `holiday_status`, `leave_type`, `number_of_days`, `number_of_hours`
- XPath or positional patches: 0

### `view_search_hr_holidays_employee_type_report`
- Name: hr.holidays.filter
- Model: `hr.leave.employee.type.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `date_from`, `employee_id`
- XPath or positional patches: 0

## Actions

- `action_hr_holidays_by_employee_and_type_report`: `server` Time off Analysis by Employee and Time Off Type

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Views]]

<!-- GENERATED:VIEWFILE -->
