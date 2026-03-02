<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/fleet_board_view.xml

- Module: [[docs/Community Addons/fleet/fleet|fleet]]
- Scope: Community Addons
- Source file: `views/fleet_board_view.xml`
- Views: 5
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `fleet_vechicle_costs_report_view_form`
- Name: fleet.vehicle.cost.report.form
- Model: `fleet.vehicle.cost.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `company_id`, `cost`, `cost_type`, `date_start`, `driver_id`, `fuel_type`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vechicle_costs_report_view_tree`
- Name: fleet.vehicle.cost.report.view.list
- Model: `fleet.vehicle.cost.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_id`, `cost`, `cost_type`, `date_start`, `driver_id`, `fuel_type`, `name`
- XPath or positional patches: 0

### `fleet_costs_report_view_graph`
- Name: fleet.vehicle.cost.view.graph
- Model: `fleet.vehicle.cost.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `cost`, `cost_type`, `date_start`
- XPath or positional patches: 0

### `fleet_costs_report_view_pivot`
- Name: fleet.vehicle.cost.view.pivot
- Model: `fleet.vehicle.cost.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `cost`, `cost_type`, `date_start`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_costs_report_view_search`
- Name: fleet.vehicle.cost.view.search
- Model: `fleet.vehicle.cost.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `date_start`, `driver_id`, `name`
- XPath or positional patches: 0

## Actions

- `fleet_costs_reporting_action`: `act_window` Costs Analysis

## Menus

- `menu_fleet_reporting_costs`: Costs
- `menu_fleet_reporting`: Reporting

## Navigation

- **Parent:** [[docs/Community Addons/fleet/Views]]

<!-- GENERATED:VIEWFILE -->
