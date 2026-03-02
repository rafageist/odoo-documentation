<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.version

- Module: [[docs/Enterprise Addons/l10n_ae_hr_payroll/l10n_ae_hr_payroll|l10n_ae_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_version.py`
- Python classes: `HrVersion`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 2, `Float` x 1, `Integer` x 1, `Monetary` x 4
- Relation fields: 0

## Sample fields

- `l10n_ae_eos_daily_salary`: `Float`
- `l10n_ae_housing_allowance`: `Monetary`
- `l10n_ae_is_computed_based_on_daily_salary`: `Boolean`
- `l10n_ae_is_dews_applied`: `Boolean`
- `l10n_ae_number_of_leave_days`: `Integer`
- `l10n_ae_other_allowances`: `Monetary`
- `l10n_ae_total_salary`: `Monetary` (compute `_compute_total_salary`)
- `l10n_ae_transportation_allowance`: `Monetary`

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_total_salary`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ae_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
