<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/hr_leave_report_calendar.xml

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Source file: `report/hr_leave_report_calendar.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `hr_leave_report_calendar_view_search`
- Name: hr.leave.report.calendar.view.search
- Model: `hr.leave.report.calendar`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `department_id`, `employee_id`, `job_id`
- XPath or positional patches: 0

### `hr_leave_report_calendar_view_form`
- Name: hr.leave.report.calendar.view.form
- Model: `hr.leave.report.calendar`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `description`, `duration_display`, `employee_id`, `holiday_status_id`, `start_datetime`
- Buttons: `action_approve`, `action_refuse`
- XPath or positional patches: 0

### `hr_leave_report_calendar_year_view`
- Name: hr.leave.report.calendar.year.view
- Model: `hr.leave.report.calendar`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 5
- Sample fields: `employee_id`, `is_hatched`, `leave_manager_id`, `name`, `state`
- XPath or positional patches: 0

### `hr_leave_report_calendar_view`
- Name: hr.leave.report.calendar.view
- Model: `hr.leave.report.calendar`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 5
- Sample fields: `employee_id`, `is_hatched`, `leave_manager_id`, `name`, `state`
- XPath or positional patches: 0

## Actions

- `action_my_days_off_dashboard_calendar`: `act_window` Dashboard
- `action_hr_holidays_dashboard`: `act_window` All Time Off

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Views]]

<!-- GENERATED:VIEWFILE -->
