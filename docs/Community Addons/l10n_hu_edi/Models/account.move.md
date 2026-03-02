<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.move

- Module: [[docs/Community Addons/l10n_hu_edi/l10n_hu_edi|l10n_hu_edi]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/account_move.py`
- Python classes: `AccountMove`

## Field footprint

- Detected fields: 10
- Field types: `Binary` x 1, `Char` x 2, `Datetime` x 1, `Html` x 1, `Integer` x 2, `Json` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `l10n_hu_edi_attachment`: `Binary`
- `l10n_hu_edi_attachment_filename`: `Char` (compute `_compute_l10n_hu_edi_attachment_filename`)
- `l10n_hu_edi_batch_upload_index`: `Integer`
- `l10n_hu_edi_message_html`: `Html` (compute `_compute_message_html`)
- `l10n_hu_edi_messages`: `Json`
- `l10n_hu_edi_send_time`: `Datetime`
- `l10n_hu_edi_state`: `Selection`
- `l10n_hu_edi_transaction_code`: `Char`
- `l10n_hu_invoice_chain_index`: `Integer`
- `l10n_hu_payment_mode`: `Selection`

## Method hints

- Detected methods: 32
- Action methods: none
- Compute methods: `_compute_expected_currency_rate`, `_compute_invoice_currency_rate`, `_compute_l10n_hu_edi_attachment_filename`, `_compute_message_html`, `_compute_need_cancel_request`, `_compute_show_reset_to_draft_button`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/l10n_hu_edi/Models]]

<!-- GENERATED:MODEL -->
