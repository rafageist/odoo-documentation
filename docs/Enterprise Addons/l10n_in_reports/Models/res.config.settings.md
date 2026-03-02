<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/l10n_in_reports/l10n_in_reports|l10n_in_reports]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 4, `Char` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_in_enet_vendor_batch_payment_feature`: `Boolean` (related `company_id.l10n_in_enet_vendor_batch_payment_feature`)
- `l10n_in_fetch_vendor_edi_feature`: `Boolean` (related `company_id.l10n_in_fetch_vendor_edi_feature`)
- `l10n_in_gst_efiling_feature`: `Boolean` (related `company_id.l10n_in_gst_efiling_feature`)
- `l10n_in_gstr_activate_einvoice_fetch`: `Selection` (related `company_id.l10n_in_gstr_activate_einvoice_fetch`)
- `l10n_in_gstr_gst_token_valid`: `Boolean` (compute `_compute_l10n_in_gstr_gst_token_valid`)
- `l10n_in_gstr_gst_username`: `Char` (comodel `GST username`, related `company_id.l10n_in_gstr_gst_username`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_l10n_in_gstr_gst_token_valid`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_in_reports/Models]]

<!-- GENERATED:MODEL -->
