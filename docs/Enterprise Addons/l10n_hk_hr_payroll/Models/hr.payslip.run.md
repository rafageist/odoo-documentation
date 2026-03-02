<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.payslip.run

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll/l10n_hk_hr_payroll|l10n_hk_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_payslip_run.py`
- Python classes: `HrPayslipRun`

## Field footprint

- Detected fields: 7
- Field types: `Binary` x 2, `Boolean` x 1, `Char` x 2, `Datetime` x 2
- Relation fields: 0

## Sample fields

- `l10n_hk_autopay`: `Boolean` (related `company_id.l10n_hk_autopay`)
- `l10n_hk_autopay_export_first_batch`: `Binary`
- `l10n_hk_autopay_export_first_batch_date`: `Datetime`
- `l10n_hk_autopay_export_first_batch_filename`: `Char`
- `l10n_hk_autopay_export_second_batch`: `Binary`
- `l10n_hk_autopay_export_second_batch_date`: `Datetime`
- `l10n_hk_autopay_export_second_batch_filename`: `Char`

## Method hints

- Detected methods: 1
- Action methods: `action_open_hsbc_autopay_wizard`
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
