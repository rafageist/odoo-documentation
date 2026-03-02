<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# fleet.vehicle

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_fleet/l10n_be_hr_payroll_fleet|l10n_be_hr_payroll_fleet]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/fleet.py`
- Python classes: `FleetVehicle`

## Field footprint

- Detected fields: 6
- Field types: `Float` x 5, `Selection` x 1
- Relation fields: 0

## Sample fields

- `atn`: `Float` (compute `_compute_car_atn`)
- `co2_fee`: `Float` (compute `_compute_co2_fee`)
- `fuel_type`: `Selection`
- `tax_deduction`: `Float` (compute `_compute_tax_deduction`)
- `total_cost`: `Float` (compute `_compute_total_cost`)
- `total_depreciated_cost`: `Float` (compute `_compute_total_depreciated_cost`)

## Method hints

- Detected methods: 14
- Action methods: none
- Compute methods: `_compute_car_atn`, `_compute_co2_fee`, `_compute_tax_deduction`, `_compute_total_cost`, `_compute_total_depreciated_cost`, `_compute_vehicle_name`
- Onchange methods: `_onchange_model_id`

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_fleet/Models]]

<!-- GENERATED:MODEL -->
