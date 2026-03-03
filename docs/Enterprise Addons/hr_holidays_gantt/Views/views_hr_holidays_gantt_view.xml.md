---
tags: [odoo, enterprise, generated, views]
---

# views/hr_holidays_gantt_view.xml

- Module: [[docs/Enterprise Addons/hr_holidays_gantt/hr_holidays_gantt|hr_holidays_gantt]]
- Scope: Enterprise Addons
- Source file: `views/hr_holidays_gantt_view.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `hr_leave_report_calendar_view_gantt`
- Name: hr.leave.report.calendar.view.gantt
- Model: `hr.leave.report.calendar`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 3
- Sample fields: `is_manager`, `name`, `state`
- Buttons: `action_approve`, `action_refuse`
- XPath or positional patches: 0

### `hr_leave_allocation_gantt_view`
- Name: hr.leave.allocation.gantt
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 1
- Sample fields: `state`
- XPath or positional patches: 0

### `hr_leave_gantt_view`
- Name: hr.leave.gantt
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 6
- Sample fields: `can_approve`, `can_refuse`, `can_validate`, `holiday_status_id`, `number_of_days`, `state`
- Buttons: `action_approve`, `action_refuse`
- XPath or positional patches: 0

## Actions

- `hr_holidays.hr_leave_action_action_approve_department`: `act_window`
- `hr_holidays.action_hr_holidays_dashboard`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_holidays_gantt/Views]]

