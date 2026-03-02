<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.payslip

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll/l10n_hk_hr_payroll|l10n_hk_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_payslip.py`
- Python classes: `HrPayslip`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 2, `Integer` x 1, `Monetary` x 5
- Relation fields: 0

## Sample fields

- `l10n_hk_713_gross`: `Monetary` (compute `_compute_gross`, store `True`)
- `l10n_hk_autopay_gross`: `Monetary` (compute `_compute_gross`, store `True`)
- `l10n_hk_average_daily_wage`: `Monetary` (compute `_compute_average_daily_wage`)
- `l10n_hk_includes_eoy_pay`: `Boolean` (compute `_compute_includes_eoy_pay`, store `True`)
- `l10n_hk_mpf_gross`: `Monetary` (compute `_compute_gross`, store `True`)
- `l10n_hk_second_batch_autopay_gross`: `Monetary` (compute `_compute_gross`, store `True`)
- `l10n_hk_use_mpf_offsetting`: `Boolean` (compute `_compute_l10n_hk_use_mpf_offsetting`, store `True`)
- `l10n_hk_worked_days_leaves_count`: `Integer` (compute `_compute_worked_days_leaves_count`)

## Method hints

- Detected methods: 20
- Action methods: `action_payslip_done`
- Compute methods: `_compute_average_daily_wage`, `_compute_gross`, `_compute_includes_eoy_pay`, `_compute_l10n_hk_use_mpf_offsetting`, `_compute_worked_days_leaves_count`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
