<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.move

- Module: [[docs/Enterprise Addons/l10n_ar_edi/l10n_ar_edi|l10n_ar_edi]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_move.py`
- Python classes: `AccountMove`

## Field footprint

- Detected fields: 15
- Field types: `Boolean` x 1, `Char` x 3, `Date` x 1, `Selection` x 8, `Text` x 2
- Relation fields: 0

## Sample fields

- `l10n_ar_afip_auth_code`: `Char` (comodel `Authorization Code`)
- `l10n_ar_afip_auth_code_due`: `Date` (comodel `Authorization Due date`)
- `l10n_ar_afip_auth_mode`: `Selection`
- `l10n_ar_afip_fce_is_cancellation`: `Boolean`
- `l10n_ar_afip_qr_code`: `Char` (compute `_compute_l10n_ar_afip_qr_code`)
- `l10n_ar_afip_result`: `Selection`
- `l10n_ar_afip_verification_result`: `Selection`
- `l10n_ar_afip_verification_type`: `Selection` (compute `_compute_l10n_ar_afip_verification_type`)
- `l10n_ar_afip_ws`: `Selection` (related `journal_id.l10n_ar_afip_ws`)
- `l10n_ar_afip_xml_request`: `Text`
- `l10n_ar_afip_xml_response`: `Text`
- `l10n_ar_currency_code`: `Char` (comodel `Currency Code`, related `currency_id.name`)
- `l10n_ar_fce_transmission_type`: `Selection` (compute `_compute_l10n_ar_fce_transmission_type`, store `True`)
- `l10n_ar_payment_foreign_currency`: `Selection` (compute `_compute_l10n_ar_payment_foreign_currency`)
- `l10n_ar_payment_foreign_currency_default`: `Selection` (related `company_id.l10n_ar_payment_foreign_currency`)

## Method hints

- Detected methods: 32
- Action methods: none
- Compute methods: `_compute_l10n_ar_afip_qr_code`, `_compute_l10n_ar_afip_verification_type`, `_compute_l10n_ar_fce_transmission_type`, `_compute_l10n_ar_payment_foreign_currency`, `_compute_show_reset_to_draft_button`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ar_edi/Models]]

<!-- GENERATED:MODEL -->
