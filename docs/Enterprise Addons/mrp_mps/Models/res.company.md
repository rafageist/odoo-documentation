<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.company

- Module: [[docs/Enterprise Addons/mrp_mps/mrp_mps|mrp_mps]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 16
- Field types: `Boolean` x 11, `Integer` x 4, `Selection` x 1
- Relation fields: 0

## Sample fields

- `manufacturing_period`: `Selection`
- `manufacturing_period_to_display_day`: `Integer` (comodel `Number of columns for the daily period to display in Master Production Schedule`)
- `manufacturing_period_to_display_month`: `Integer` (comodel `Number of columns for the monthly period to display in Master Production Schedule`)
- `manufacturing_period_to_display_week`: `Integer` (comodel `Number of columns for the weekly period to display in Master Production Schedule`)
- `manufacturing_period_to_display_year`: `Integer` (comodel `Number of columns for the yearly period to display in Master Production Schedule`)
- `mrp_mps_show_actual_demand`: `Boolean` (comodel `Display Actual Demand`)
- `mrp_mps_show_actual_demand_year_minus_1`: `Boolean` (comodel `Display Actual Demand Last Year`)
- `mrp_mps_show_actual_demand_year_minus_2`: `Boolean` (comodel `Display Actual Demand Before Year`)
- `mrp_mps_show_actual_replenishment`: `Boolean` (comodel `Display Actual Replenishment`)
- `mrp_mps_show_available_to_promise`: `Boolean` (comodel `Display Available to Promise`)
- `mrp_mps_show_demand_forecast`: `Boolean` (comodel `Display Demand Forecast`)
- `mrp_mps_show_indirect_actual_demand`: `Boolean` (comodel `Display Indirect Actual Demand`)
- `mrp_mps_show_indirect_demand`: `Boolean` (comodel `Display Indirect Demand`)
- `mrp_mps_show_safety_stock`: `Boolean` (comodel `Display Safety Stock`)
- `mrp_mps_show_starting_inventory`: `Boolean` (comodel `Display Starting Inventory`)
- `mrp_mps_show_to_replenish`: `Boolean` (comodel `Display To Replenish`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_mps/Models]]

<!-- GENERATED:MODEL -->
