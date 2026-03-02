<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.payslip

- Module: [[docs/Enterprise Addons/l10n_lu_hr_payroll/l10n_lu_hr_payroll|l10n_lu_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_payslip.py`
- Python classes: `HrPayslip`

## Field footprint

- Detected fields: 20
- Field types: `Boolean` x 4, `Char` x 1, `Float` x 6, `Monetary` x 8, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_lu_deduction_ac_ae_daily`: `Monetary` (compute `_compute_l10n_lu_deduction_ac_ae_daily`, store `True`)
- `l10n_lu_deduction_amd_daily`: `Monetary` (compute `_compute_l10n_lu_deduction_amd_daily`, store `True`)
- `l10n_lu_deduction_ce_daily`: `Monetary` (compute `_compute_l10n_lu_deduction_ce_daily`, store `True`)
- `l10n_lu_deduction_ds_daily`: `Monetary` (compute `_compute_l10n_lu_deduction_ds_daily`, store `True`)
- `l10n_lu_deduction_fd_daily`: `Monetary` (compute `_compute_l10n_lu_deduction_fd_daily`, store `True`)
- `l10n_lu_deduction_fo_daily`: `Monetary` (compute `_compute_l10n_lu_deduction_fo_daily`, store `True`)
- `l10n_lu_effective_taxable_days`: `Float` (compute `_compute_taxable_days`)
- `l10n_lu_is_monthly`: `Boolean` (compute `_compute_taxable_days`)
- `l10n_lu_month_taxable_days`: `Float` (compute `_compute_taxable_days`)
- `l10n_lu_package_fds_daily`: `Monetary` (compute `_compute_l10n_lu_package_fds_daily`, store `True`)
- `l10n_lu_package_ffo_daily`: `Monetary` (compute `_compute_l10n_lu_package_ffo_daily`, store `True`)
- `l10n_lu_period_taxable_days`: `Float` (compute `_compute_taxable_days`)
- `l10n_lu_presence_prorata`: `Float` (compute `_compute_prorated_wage`)
- `l10n_lu_prorated_wage`: `Float` (compute `_compute_prorated_wage`)
- `l10n_lu_tax_classification`: `Selection` (compute `_compute_l10n_lu_tax_classification`, store `True`)
- `l10n_lu_tax_credit_cim`: `Boolean` (compute `_compute_l10n_lu_tax_credit_cim`, store `True`)
- `l10n_lu_tax_credit_cip`: `Boolean` (compute `_compute_l10n_lu_tax_credit_cip`, store `True`)
- `l10n_lu_tax_credit_cis`: `Boolean` (compute `_compute_l10n_lu_tax_credit_cis`, store `True`)
- `l10n_lu_tax_id_number`: `Char` (compute `_compute_l10n_lu_tax_id_number`, store `True`)
- `l10n_lu_tax_rate_no_classification`: `Float` (compute `_compute_l10n_lu_tax_id_number`, store `True`)

## Method hints

- Detected methods: 22
- Action methods: none
- Compute methods: `_compute_l10n_lu_deduction_ac_ae_daily`, `_compute_l10n_lu_deduction_amd_daily`, `_compute_l10n_lu_deduction_ce_daily`, `_compute_l10n_lu_deduction_ds_daily`, `_compute_l10n_lu_deduction_fd_daily`, `_compute_l10n_lu_deduction_fo_daily`, `_compute_l10n_lu_package_fds_daily`, `_compute_l10n_lu_package_ffo_daily`, and 8 more
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_lu_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
