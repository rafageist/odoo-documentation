---
tags: [odoo, enterprise, generated, views]
---

# report/planning_analysis_report_views.xml

- Module: [[docs/Enterprise Addons/project_timesheet_forecast_sale/project_timesheet_forecast_sale|project_timesheet_forecast_sale]]
- Scope: Enterprise Addons
- Source file: `report/planning_analysis_report_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `planning_slot_report_view_pivot_inherit_project_timesheet_forecast_sale`
- Name: planning.slot.pivot.inherit.timesheet
- Model: `planning.analysis.report`
- Type: inferred from arch
- Inherits: `project_timesheet_forecast.planning_slot_report_view_pivot_inherit_project_timesheet_forecast`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `billable_allocated_hours`, `non_billable_allocated_hours`
- XPath or positional patches: 1

### `planning_slot_report_view_graph_inherit_project_timesheet_forecast_sale`
- Name: planning.slot.report.view.graph.inherit
- Model: `planning.analysis.report`
- Type: inferred from arch
- Inherits: `planning.planning_slot_report_view_graph`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `billable_allocated_hours`, `non_billable_allocated_hours`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_timesheet_forecast_sale/Views]]

