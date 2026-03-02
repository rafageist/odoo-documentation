<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.batch.payment

- Module: [[docs/Enterprise Addons/l10n_uk_bacs/l10n_uk_bacs|l10n_uk_bacs]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_batch_payment.py`
- Python classes: `AccountBatchPayment`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 1, `Char` x 1, `Date` x 2
- Relation fields: 0

## Sample fields

- `bacs_expiry_date`: `Date`
- `bacs_multi_mode`: `Boolean`
- `bacs_processing_date`: `Date`
- `bacs_submission_serial`: `Char` (store `True`)

## Method hints

- Detected methods: 8
- Action methods: none
- Compute methods: `_compute_bacs_submission_serial`
- Onchange methods: `_compute_bacs_submission_serial`

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_uk_bacs/Models]]

<!-- GENERATED:MODEL -->
