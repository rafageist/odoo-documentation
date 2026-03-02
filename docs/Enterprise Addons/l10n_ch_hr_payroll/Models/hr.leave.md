<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.leave

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_leave.py`
- Python classes: `HrLeave`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 4, `Float` x 2
- Relation fields: 0

## Sample fields

- `l10n_ch_continued_pay_percentage`: `Float` (comodel `Continued Pay %`)
- `l10n_ch_disability_percentage`: `Float` (comodel `Disability %`)
- `l10n_ch_lpp_interruption`: `Boolean` (comodel `LPP Contributions Interruption`)
- `l10n_ch_pay_interruption`: `Boolean` (comodel `Pay Interruption`)
- `l10n_ch_swissdec_payroll_impact`: `Boolean` (related `holiday_status_id.l10n_ch_swissdec_payroll_impact`)
- `l10n_ch_swissdec_work_interruption`: `Boolean` (compute `_compute_l10n_ch_swissdec_work_interruption`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_l10n_ch_swissdec_work_interruption`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
