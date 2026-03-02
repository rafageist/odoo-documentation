<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/l10n_br_edi_pos/l10n_br_edi_pos|l10n_br_edi_pos]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 1, `Char` x 5, `Integer` x 1
- Relation fields: 0

## Sample fields

- `l10n_br_edi_csc_identifier`: `Char` (related `company_id.l10n_br_edi_csc_identifier`)
- `l10n_br_edi_csc_number`: `Char` (related `company_id.l10n_br_edi_csc_number`)
- `l10n_br_edi_qr_url_override`: `Char` (related `company_id.l10n_br_edi_qr_url_override`)
- `l10n_br_edi_url_key_override`: `Char` (related `company_id.l10n_br_edi_url_key_override`)
- `l10n_br_nfce_next_number`: `Integer` (related `pos_config_id.order_seq_id.number_next_actual`)
- `pos_l10n_br_invoice_serial`: `Char` (related `pos_config_id.l10n_br_invoice_serial`)
- `pos_l10n_br_is_nfce`: `Boolean` (related `pos_config_id.l10n_br_is_nfce`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_br_edi_pos/Models]]

<!-- GENERATED:MODEL -->
