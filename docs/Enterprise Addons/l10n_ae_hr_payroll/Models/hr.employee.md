<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.employee

- Module: [[docs/Enterprise Addons/l10n_ae_hr_payroll/l10n_ae_hr_payroll|l10n_ae_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_employee.py`
- Python classes: `HrEmployee`

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 2, `Float` x 4, `Integer` x 1, `Monetary` x 3
- Relation fields: 0

## Sample fields

- `l10n_ae_annual_leave_days_taken`: `Float` (compute `_compute_l10n_ae_annual_leave_days`)
- `l10n_ae_annual_leave_days_total`: `Float` (compute `_compute_l10n_ae_annual_leave_days`)
- `l10n_ae_eos_daily_salary`: `Float` (related `version_id.l10n_ae_eos_daily_salary`)
- `l10n_ae_housing_allowance`: `Monetary` (related `version_id.l10n_ae_housing_allowance`)
- `l10n_ae_is_computed_based_on_daily_salary`: `Boolean` (related `version_id.l10n_ae_is_computed_based_on_daily_salary`)
- `l10n_ae_is_dews_applied`: `Boolean` (related `version_id.l10n_ae_is_dews_applied`)
- `l10n_ae_number_of_leave_days`: `Integer` (related `version_id.l10n_ae_number_of_leave_days`)
- `l10n_ae_other_allowances`: `Monetary` (related `version_id.l10n_ae_other_allowances`)
- `l10n_ae_total_unpaid_days`: `Float` (compute `_compute_l10n_ae_total_unpaid_days`)
- `l10n_ae_transportation_allowance`: `Monetary` (related `version_id.l10n_ae_transportation_allowance`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_l10n_ae_annual_leave_days`, `_compute_l10n_ae_total_unpaid_days`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ae_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
