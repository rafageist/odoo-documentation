<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.batch.payment

- Module: [[docs/Enterprise Addons/l10n_us_direct_deposit/l10n_us_direct_deposit|l10n_us_direct_deposit]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_batch_payment.py`
- Python classes: `AccountBatchPayment`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `wise_batch_identifier`: `Char`
- `wise_payment_status`: `Selection`
- `wise_payments_enabled`: `Boolean` (compute `_compute_wise_payments_enabled`)

## Method hints

- Detected methods: 9
- Action methods: none
- Compute methods: `_compute_wise_payments_enabled`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_us_direct_deposit/Models]]

<!-- GENERATED:MODEL -->
