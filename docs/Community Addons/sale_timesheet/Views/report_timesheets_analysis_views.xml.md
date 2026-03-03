---
tags: [odoo, community, generated, views]
---

# report/timesheets_analysis_views.xml

- Module: [[docs/Community Addons/sale_timesheet/sale_timesheet|sale_timesheet]]
- Scope: Community Addons
- Source file: `report/timesheets_analysis_views.xml`
- Views: 12
- Actions: 4
- Menus: 1
- Rules: 0

## View records

### `hr_timesheet_report_search_sale_timesheet`
- Name: timesheets.analysis.report.search
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Inherits: `sale_timesheet.timesheet_view_search`
- Root tag: `search`
- Field references: 1
- Sample fields: `so_line`
- XPath or positional patches: 3

### `timesheets_analysis_report_graph_invoice_type`
- Name: timesheets.analysis.report.graph
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 5
- Sample fields: `amount`, `billable_time`, `non_billable_time`, `timesheet_invoice_type`, `unit_amount`
- XPath or positional patches: 0

### `timesheets_analysis_report_pivot_invoice_type`
- Name: timesheets.analysis.report.pivot
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 6
- Sample fields: `amount`, `billable_time`, `date`, `non_billable_time`, `timesheet_invoice_type`, `unit_amount`
- XPath or positional patches: 0

### `timesheets_analysis_report_graph_task_inherit`
- Name: timesheets.analysis.report.graph.task
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheets_analysis_report_graph_task`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `billable_time`, `non_billable_time`
- XPath or positional patches: 1

### `timesheets_analysis_report_pivot_task_inherit`
- Name: timesheets.analysis.report.pivot.task
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheets_analysis_report_pivot_task`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `billable_time`, `non_billable_time`
- XPath or positional patches: 1

### `timesheets_analysis_report_graph_project_inherit`
- Name: timesheets.analysis.report.graph.project
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheets_analysis_report_graph_project`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `billable_time`, `non_billable_time`
- XPath or positional patches: 1

### `timesheets_analysis_report_pivot_project_inherit`
- Name: timesheets.analysis.report.pivot.project
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheets_analysis_report_pivot_project`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `billable_time`, `non_billable_time`
- XPath or positional patches: 1

### `timesheets_analysis_report_graph_timesheet_grid`
- Name: timesheets.analysis.report.graph
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheets_analysis_report_graph_employee`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `billable_time`, `non_billable_time`
- XPath or positional patches: 1

### `timesheets_analysis_report_graph_inherit`
- Name: timesheets.analysis.report.graph
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheets_analysis_report_pivot_employee`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `billable_time`, `non_billable_time`
- XPath or positional patches: 1

### `timesheets_analysis_report_pivot_inherit`
- Name: timesheets.analysis.report.pivot
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheets_analysis_report_pivot_employee`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `billable_time`, `non_billable_time`
- XPath or positional patches: 1

### `timesheete_analysis_report_form`
- Name: timesheets.analysis.report.form
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheets_analysis_report_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `so_line`
- XPath or positional patches: 1

### `timesheets_analysis_report_list_inherited`
- Name: timesheets.analysis.report.list.inherited
- Model: `timesheets.analysis.report`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheets_analysis_report_list`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `margin`, `so_line`, `timesheet_invoice_id`, `timesheet_invoice_type`, `timesheet_revenues`
- XPath or positional patches: 1

## Actions

- `timesheet_action_view_report_by_billing_rate_list`: `view`
- `timesheet_action_view_report_by_billing_rate_graph`: `view`
- `timesheet_action_view_report_by_billing_rate_pivot`: `view`
- `timesheet_action_billing_report`: `act_window` Timesheets by Billing Type

## Menus

- `menu_timesheet_billing_analysis`: By Billing Type

## Navigation

- **Parent:** [[docs/Community Addons/sale_timesheet/Views]]

