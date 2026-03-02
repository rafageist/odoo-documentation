<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.version

- Module: [[docs/Enterprise Addons/l10n_lu_hr_payroll/l10n_lu_hr_payroll|l10n_lu_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_version.py`
- Python classes: `HrVersion`

## Field footprint

- Detected fields: 41
- Field types: `Boolean` x 4, `Char` x 1, `Float` x 3, `Monetary` x 31, `Selection` x 2
- Relation fields: 0

## Sample fields

- `l10n_lu_alw_vehicle`: `Monetary`
- `l10n_lu_bik_meal_voucher_exceeding_amount`: `Monetary` (compute `_compute_l10n_lu_meal_voucher_employer_cost`)
- `l10n_lu_bik_other_benefits`: `Monetary`
- `l10n_lu_bik_vehicle`: `Monetary`
- `l10n_lu_bik_vehicle_vat_included`: `Boolean`
- `l10n_lu_current_index`: `Float` (compute `_compute_indexed_wage`)
- `l10n_lu_deduction_ac_ae_daily`: `Monetary`
- `l10n_lu_deduction_ac_ae_monthly`: `Monetary` (compute `_compute_l10n_lu_deduction_ac_ae`)
- `l10n_lu_deduction_ac_ae_yearly`: `Monetary` (compute `_compute_l10n_lu_deduction_ac_ae`)
- `l10n_lu_deduction_amd_daily`: `Monetary`
- `l10n_lu_deduction_amd_monthly`: `Monetary` (compute `_compute_l10n_lu_deduction_amd`)
- `l10n_lu_deduction_amd_yearly`: `Monetary` (compute `_compute_l10n_lu_deduction_amd`)
- `l10n_lu_deduction_ce_daily`: `Monetary`
- `l10n_lu_deduction_ce_monthly`: `Monetary` (compute `_compute_l10n_lu_deduction_ce`)
- `l10n_lu_deduction_ce_yearly`: `Monetary` (compute `_compute_l10n_lu_deduction_ce`)
- `l10n_lu_deduction_ds_daily`: `Monetary`
- `l10n_lu_deduction_ds_monthly`: `Monetary` (compute `_compute_l10n_lu_deduction_ds`)
- `l10n_lu_deduction_ds_yearly`: `Monetary` (compute `_compute_l10n_lu_deduction_ds`)
- `l10n_lu_deduction_fd_daily`: `Monetary`
- `l10n_lu_deduction_fd_monthly`: `Monetary` (compute `_compute_l10n_lu_deduction_fd`)

## Method hints

- Detected methods: 11
- Action methods: none
- Compute methods: `_compute_indexed_wage`, `_compute_l10n_lu_deduction_ac_ae`, `_compute_l10n_lu_deduction_amd`, `_compute_l10n_lu_deduction_ce`, `_compute_l10n_lu_deduction_ds`, `_compute_l10n_lu_deduction_fd`, `_compute_l10n_lu_deduction_fo`, `_compute_l10n_lu_meal_voucher_employer_cost`, and 2 more
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_lu_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
