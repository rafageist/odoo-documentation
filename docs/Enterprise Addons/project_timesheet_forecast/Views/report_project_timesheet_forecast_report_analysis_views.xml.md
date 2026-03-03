---
tags: [odoo, enterprise, generated, views]
---

# report/project_timesheet_forecast_report_analysis_views.xml

- Module: [[docs/Enterprise Addons/project_timesheet_forecast/project_timesheet_forecast|project_timesheet_forecast]]
- Scope: Enterprise Addons
- Source file: `report/project_timesheet_forecast_report_analysis_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 1

## View records

### `project_timesheet_forecast_report_view_search`
- Name: timesheet.forecast.report.search
- Model: `project.timesheet.forecast.report.analysis`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `employee_id`, `entry_date`, `project_id`
- XPath or positional patches: 0

### `project_timesheet_forecast_report_analysis_view_tree`
- Name: project.timesheet.forecast.report.analysis.view.list
- Model: `project.timesheet.forecast.report.analysis`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_id`, `difference`, `effective_hours`, `employee_id`, `entry_date`, `planned_hours`, `project_id`
- XPath or positional patches: 0

### `project_timesheet_forecast_report_view_graph`
- Name: timesheet.forecast.report.graph
- Model: `project.timesheet.forecast.report.analysis`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 6
- Sample fields: `difference`, `effective_costs`, `effective_hours`, `entry_date`, `planned_costs`, `planned_hours`
- XPath or positional patches: 0

### `project_timesheet_forecast_report_view_pivot`
- Name: timesheet.forecast.report.pivot
- Model: `project.timesheet.forecast.report.analysis`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 7
- Sample fields: `difference`, `effective_costs`, `effective_hours`, `employee_id`, `entry_date`, `planned_costs`, `planned_hours`
- XPath or positional patches: 0

## Actions

- `project_timesheet_forecast_report_action`: `act_window` Planning / Timesheets Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_timesheet_forecast/Views]]

