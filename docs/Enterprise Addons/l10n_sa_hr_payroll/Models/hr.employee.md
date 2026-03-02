<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.employee

- Module: [[docs/Enterprise Addons/l10n_sa_hr_payroll/l10n_sa_hr_payroll|l10n_sa_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_employee.py`
- Python classes: `HrEmployee`

## Field footprint

- Detected fields: 8
- Field types: `Char` x 2, `Float` x 2, `Integer` x 1, `Monetary` x 3
- Relation fields: 0

## Sample fields

- `l10n_sa_employee_code`: `Char`
- `l10n_sa_housing_allowance`: `Monetary` (related `version_id.l10n_sa_housing_allowance`)
- `l10n_sa_leaves_count_compensable`: `Float` (store `False`)
- `l10n_sa_number_of_days`: `Integer` (related `version_id.l10n_sa_number_of_days`)
- `l10n_sa_other_allowances`: `Monetary` (related `version_id.l10n_sa_other_allowances`)
- `l10n_sa_remaining_annual_leave_balance`: `Float` (compute `_compute_l10n_sa_remaining_annual_leave_balance`)
- `l10n_sa_transportation_allowance`: `Monetary` (related `version_id.l10n_sa_transportation_allowance`)
- `l10n_sa_wps_description`: `Char` (related `version_id.l10n_sa_wps_description`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_l10n_sa_remaining_annual_leave_balance`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_sa_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
