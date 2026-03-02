<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.move

- Module: [[docs/Community Addons/l10n_eg_edi_eta/l10n_eg_edi_eta|l10n_eg_edi_eta]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/account_move.py`
- Python classes: `AccountMove`

## Field footprint

- Detected fields: 7
- Field types: `Binary` x 1, `Boolean` x 1, `Char` x 4, `Datetime` x 1
- Relation fields: 0

## Sample fields

- `l10n_eg_eta_json_doc_file`: `Binary`
- `l10n_eg_is_signed`: `Boolean`
- `l10n_eg_long_id`: `Char` (compute `_compute_eta_long_id`)
- `l10n_eg_qr_code`: `Char` (compute `_compute_eta_qr_code_str`)
- `l10n_eg_signing_time`: `Datetime` (comodel `Signing Time`)
- `l10n_eg_submission_number`: `Char` (compute `_compute_eta_response_data`, store `True`)
- `l10n_eg_uuid`: `Char` (compute `_compute_eta_response_data`, store `True`)

## Method hints

- Detected methods: 9
- Action methods: `action_get_eta_invoice_pdf`, `action_post_sign_invoices`
- Compute methods: `_compute_eta_long_id`, `_compute_eta_qr_code_str`, `_compute_eta_response_data`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/l10n_eg_edi_eta/Models]]

<!-- GENERATED:MODEL -->
