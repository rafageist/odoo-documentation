<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_au.super.stream

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_api/l10n_au_hr_payroll_api|l10n_au_hr_payroll_api]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/l10n_au_superstream.py`
- Python classes: `L10n_auSuperStream`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Char` x 2, `Integer` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `days_funds_update`: `Integer` (compute `_compute_funds_update`)
- `message_id`: `Char` (comodel `API Message ID`)
- `payment_ref`: `Char` (comodel `Direct Debit Payment Ref.`)
- `payment_status`: `Selection`
- `source_payment_status`: `Selection`
- `to_be_replaced`: `Boolean` (comodel `To be Replaced`, compute `_compute_to_be_replaced`)

## Method hints

- Detected methods: 12
- Action methods: `action_cancel`, `action_check_cancelation_type`, `action_open_payment`, `action_register_super_payment`, `action_resubmit_failed`, `action_update_funds`
- Compute methods: `_compute_funds_update`, `_compute_to_be_replaced`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_api/Models]]

<!-- GENERATED:MODEL -->
