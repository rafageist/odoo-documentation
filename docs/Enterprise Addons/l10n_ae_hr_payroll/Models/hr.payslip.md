<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.payslip

- Module: [[docs/Enterprise Addons/l10n_ae_hr_payroll/l10n_ae_hr_payroll|l10n_ae_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_payslip.py`
- Python classes: `HrPayslip`

## Field footprint

- Detected fields: 4
- Field types: `Float` x 2, `Monetary` x 2
- Relation fields: 0

## Sample fields

- `l10n_ae_basic_salary`: `Monetary` (compute `_compute_l10n_ae_basic_salary`)
- `l10n_ae_hourly_wage`: `Monetary` (compute `_compute_l10n_ae_hourly_wage`)
- `l10n_ae_hours_worked`: `Float` (compute `_compute_l10n_ae_worked_values`)
- `l10n_ae_total_paid_hours`: `Float` (compute `_compute_l10n_ae_worked_values`)

## Method hints

- Detected methods: 11
- Action methods: `action_payslip_payment_report`
- Compute methods: `_compute_input_line_ids`, `_compute_l10n_ae_basic_salary`, `_compute_l10n_ae_hourly_wage`, `_compute_l10n_ae_worked_values`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ae_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
