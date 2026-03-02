<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.payslip

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_account/l10n_au_hr_payroll_account|l10n_au_hr_payroll_account]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_payslip.py`
- Python classes: `HrPayslip`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 2, `Integer` x 1, `Monetary` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `has_superstream`: `Boolean` (compute `_compute_has_superstream`)
- `l10n_au_finalised`: `Boolean` (comodel `Finalised`)
- `l10n_au_stp_count`: `Integer` (compute `_compute_stp_count`)
- `l10n_au_stp_status`: `Selection` (compute `_compute_stp_status`)
- `net_wage`: `Monetary`

## Method hints

- Detected methods: 23
- Action methods: `action_open_payslip_stp`, `action_open_superstream`, `action_payslip_cancel`, `action_payslip_done`, `action_payslip_draft`, `action_payslip_payment_report`, `action_register_payment`
- Compute methods: `_compute_has_superstream`, `_compute_payslip_ytd_totals`, `_compute_stp_count`, `_compute_stp_status`, `_compute_worked_days_ytd`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_account/Models]]

<!-- GENERATED:MODEL -->
