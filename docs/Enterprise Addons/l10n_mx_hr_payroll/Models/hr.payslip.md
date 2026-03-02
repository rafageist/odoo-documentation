<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.payslip

- Module: [[docs/Enterprise Addons/l10n_mx_hr_payroll/l10n_mx_hr_payroll|l10n_mx_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_payslip.py`
- Python classes: `HrPayslip`

## Field footprint

- Detected fields: 4
- Field types: `Float` x 2, `Integer` x 2
- Relation fields: 0

## Sample fields

- `l10n_mx_daily_salary`: `Float` (comodel `MX: Daily Salary`, compute `_compute_daily_salary`)
- `l10n_mx_days_of_year`: `Integer` (comodel `MX: Days of the Year`, compute `_compute_days_of_year`)
- `l10n_mx_integration_factor`: `Float` (comodel `MX: Integration Factor`, compute `_compute_integration_factor`)
- `l10n_mx_years_worked`: `Integer` (comodel `MX: Years Worked`, compute `_compute_integration_factor`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_daily_salary`, `_compute_days_of_year`, `_compute_integration_factor`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
