<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/planning_report_views.xml

- Module: [[docs/Enterprise Addons/planning/planning|planning]]
- Scope: Enterprise Addons
- Source file: `views/planning_report_views.xml`
- Views: 3
- Actions: 3
- Menus: 2
- Rules: 0

## View records

### `planning_analysis_report_view_search`
- Name: planning.slot.report.search
- Model: `planning.analysis.report`
- Type: inferred from arch
- Inherits: `planning_view_search_base`
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 1

### `planning_slot_report_view_graph`
- Name: planning.slot.report.graph
- Model: `planning.analysis.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `allocated_hours`, `resource_id`, `start_datetime`
- XPath or positional patches: 0

### `planning_slot_report_view_pivot`
- Name: planning.slot.report.pivot
- Model: `planning.analysis.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `allocated_hours`, `start_datetime`
- XPath or positional patches: 0

## Actions

- `planning_slot_report_action_view_graph`: `view`
- `planning_slot_report_action_view_pivot`: `view`
- `planning_report_action_analysis`: `act_window` Planning Analysis

## Menus

- `planning_menu_planning_analysis`: Planning Analysis
- `planning_menu_reporting`: Reporting

## Navigation

- **Parent:** [[docs/Enterprise Addons/planning/Views]]

<!-- GENERATED:VIEWFILE -->
