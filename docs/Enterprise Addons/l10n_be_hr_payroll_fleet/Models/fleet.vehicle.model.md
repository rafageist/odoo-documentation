<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# fleet.vehicle.model

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_fleet/l10n_be_hr_payroll_fleet|l10n_be_hr_payroll_fleet]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/fleet.py`
- Python classes: `FleetVehicleModel`

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 1, `Char` x 1, `Float` x 7
- Relation fields: 0

## Sample fields

- `can_be_requested`: `Boolean`
- `co2_fee`: `Float` (compute `_compute_co2_fee`)
- `current_country_code`: `Char` (compute `_compute_current_country_code`)
- `default_atn`: `Float` (compute `_compute_atn`)
- `default_car_value`: `Float`
- `default_co2`: `Float` (compute `_compute_default_co2`, store `True`)
- `default_recurring_cost_amount_depreciated`: `Float`
- `default_total_depreciated_cost`: `Float` (compute `_compute_default_total_depreciated_cost`)
- `tax_deduction`: `Float` (compute `_compute_tax_deduction`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_atn`, `_compute_co2_fee`, `_compute_current_country_code`, `_compute_default_co2`, `_compute_default_total_depreciated_cost`, `_compute_tax_deduction`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_fleet/Models]]

<!-- GENERATED:MODEL -->
