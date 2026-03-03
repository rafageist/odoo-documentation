---
tags: [odoo, enterprise, generated, views]
---

# report/planning_analysis_report_views.xml

- Module: [[docs/Enterprise Addons/project_timesheet_forecast/project_timesheet_forecast|project_timesheet_forecast]]
- Scope: Enterprise Addons
- Source file: `report/planning_analysis_report_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `planning_slot_report_view_graph_inherit_project_timesheet_forecast`
- Name: planning.slot.pivot.inherit.timesheet
- Model: `planning.analysis.report`
- Type: inferred from arch
- Inherits: `planning.planning_slot_report_view_graph`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `effective_hours`, `remaining_hours`
- XPath or positional patches: 1

### `planning_slot_report_view_pivot_inherit_project_timesheet_forecast`
- Name: planning.slot.pivot.inherit.timesheet
- Model: `planning.analysis.report`
- Type: inferred from arch
- Inherits: `planning.planning_slot_report_view_pivot`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `effective_hours`, `remaining_hours`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_timesheet_forecast/Views]]

