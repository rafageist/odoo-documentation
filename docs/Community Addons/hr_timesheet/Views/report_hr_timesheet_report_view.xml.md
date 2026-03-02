<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/hr_timesheet_report_view.xml

- Module: [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]
- Scope: Community Addons
- Source file: `report/hr_timesheet_report_view.xml`
- Views: 9
- Actions: 12
- Menus: 0
- Rules: 0

## View records

### `hr_timesheet_report_search`
- Name: timesheets.analysis.report.search
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_search`
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 1

### `timesheets_analysis_report_graph_task`
- Name: timesheets.analysis.report.graph
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `amount`, `project_id`, `task_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheets_analysis_report_pivot_task`
- Name: timesheets.analysis.report.pivot
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `amount`, `date`, `project_id`, `task_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheets_analysis_report_graph_project`
- Name: timesheets.analysis.report.graph
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `amount`, `project_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheets_analysis_report_pivot_project`
- Name: timesheets.analysis.report.pivot
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `amount`, `date`, `project_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheets_analysis_report_graph_employee`
- Name: timesheets.analysis.report.graph
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `amount`, `employee_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheets_analysis_report_pivot_employee`
- Name: timesheets.analysis.report.pivot
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `amount`, `date`, `employee_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheets_analysis_report_form`
- Name: timesheets.analysis.report.form
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `amount`, `date`, `employee_id`, `name`, `project_id`, `task_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheets_analysis_report_list`
- Name: timesheets.analysis.report.list
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `amount`, `currency_id`, `date`, `employee_id`, `project_id`, `task_id`, `unit_amount`
- XPath or positional patches: 0

## Actions

- `timesheet_action_view_report_by_task_list`: `view`
- `timesheet_action_view_report_by_task_graph`: `view`
- `timesheet_action_view_report_by_task_pivot`: `view`
- `timesheet_action_report_by_task`: `act_window` Timesheets by Task
- `timesheet_action_view_report_by_project_list`: `view`
- `timesheet_action_view_report_by_project_graph`: `view`
- `timesheet_action_view_report_by_project_pivot`: `view`
- `timesheet_action_report_by_project`: `act_window` Timesheets by Project
- `timesheet_action_view_report_by_employee_list`: `view`
- `timesheet_action_view_report_by_employee_graph`: `view`
- `act_hr_timesheet_report_pivot`: `view`
- `act_hr_timesheet_report`: `act_window` Timesheets by Employee

## Navigation

- **Parent:** [[docs/Community Addons/hr_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
