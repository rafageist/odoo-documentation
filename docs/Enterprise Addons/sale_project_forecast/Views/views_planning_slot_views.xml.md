<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/planning_slot_views.xml

- Module: [[docs/Enterprise Addons/sale_project_forecast/sale_project_forecast|sale_project_forecast]]
- Scope: Enterprise Addons
- Source file: `views/planning_slot_views.xml`
- Views: 1
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `planning_slot_view_search_inherit_sale_project_forecast`
- Name: planning.slot.search.inherit.sale.project.forecast
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `sale_planning.planning_slot_view_search_inherit_sale_planning`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

## Actions

- `sale_planning.sale_planning_action_schedule_by_sale_order`: `act_window`
- `project_forecast.project_forecast_action_schedule_by_employee`: `act_window`
- `project_forecast.planning_action_schedule_by_project`: `act_window`
- `planning.planning_action_schedule_by_role`: `act_window`
- `planning.planning_action_schedule_by_resource`: `act_window`
- `planning.planning_action_my_calendar`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_project_forecast/Views]]

<!-- GENERATED:VIEWFILE -->
