<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.payment

- Module: [[docs/Enterprise Addons/account_iso20022/account_iso20022|account_iso20022]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_payment.py`
- Python classes: `AccountPayment`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Char` x 2, `Selection` x 3
- Relation fields: 0

## Sample fields

- `end_to_end_uuid`: `Char` (compute `_compute_end_to_end_uuid`, store `True`)
- `iso20022_charge_bearer`: `Selection` (compute `_compute_iso20022_charge_bearer`, store `True`)
- `iso20022_priority`: `Selection` (compute `_compute_payment_method_priority`, store `True`)
- `iso20022_uetr`: `Char` (compute `_compute_iso20022_uetr`, store `True`)
- `payment_method_is_iso20022`: `Boolean` (related `payment_method_line_id.payment_method_id.is_iso20022`)
- `sepa_pain_version`: `Selection` (related `journal_id.sepa_pain_version`)

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_end_to_end_uuid`, `_compute_iso20022_charge_bearer`, `_compute_iso20022_uetr`, `_compute_payment_method_priority`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_iso20022/Models]]

<!-- GENERATED:MODEL -->
