<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.move.reversal

- Module: [[docs/Community Addons/l10n_tw_edi_ecpay/l10n_tw_edi_ecpay|l10n_tw_edi_ecpay]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `wizard/account_move_reversal.py`
- Python classes: `AccountMoveReversal`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 1, `Char` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `l10n_tw_edi_allowance_notify_way`: `Selection`
- `l10n_tw_edi_ecpay_invoice_id`: `Char` (compute `_compute_from_moves`)
- `l10n_tw_edi_is_b2b`: `Boolean` (compute `_compute_from_moves`)
- `l10n_tw_edi_refund_agreement_type`: `Selection`

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_from_moves`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/l10n_tw_edi_ecpay/Models]]

<!-- GENERATED:MODEL -->
