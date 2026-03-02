<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.payslip

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_payslip.py`
- Python classes: `HrPayslip`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 3, `Char` x 1, `Float` x 1, `Integer` x 3
- Relation fields: 0

## Sample fields

- `l10n_be_has_eco_vouchers`: `Boolean` (compute `_compute_l10n_be_has_eco_vouchers`)
- `l10n_be_is_december`: `Boolean` (compute `_compute_l10n_be_is_december`)
- `l10n_be_is_double_pay`: `Boolean` (compute `_compute_l10n_be_is_double_pay`)
- `l10n_be_max_seizable_amount`: `Float` (compute `_compute_l10n_be_max_seizable_amount`)
- `l10n_be_max_seizable_warning`: `Char` (compute `_compute_l10n_be_max_seizable_amount`)
- `meal_voucher_count`: `Integer` (compute `_compute_work_entry_dependent_benefits`)
- `private_car_missing_days`: `Integer` (compute `_compute_work_entry_dependent_benefits`)
- `representation_fees_missing_days`: `Integer` (compute `_compute_work_entry_dependent_benefits`)

## Method hints

- Detected methods: 54
- Action methods: `action_payslip_done`
- Compute methods: `_compute_input_line_ids`, `_compute_l10n_be_has_eco_vouchers`, `_compute_l10n_be_is_december`, `_compute_l10n_be_is_double_pay`, `_compute_l10n_be_max_seizable_amount`, `_compute_number_complete_months_of_work`, `_compute_presence_prorated_fixed_wage`, `_compute_work_entry_dependent_benefits`, and 1 more
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
