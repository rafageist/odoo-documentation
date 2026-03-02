<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.return

- Module: [[docs/Enterprise Addons/l10n_in_edi_gstr/l10n_in_edi_gstr|l10n_in_edi_gstr]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_return.py`
- Python classes: `AccountReturn`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 4
- Relation fields: 0

## Sample fields

- `l10n_in_edi_feature_enabled`: `Boolean` (related `company_id.l10n_in_edi_feature`)
- `l10n_in_gst_efiling_feature_enabled`: `Boolean` (related `company_id.l10n_in_gst_efiling_feature`)
- `l10n_in_gstr1_include_einvoice`: `Boolean`
- `l10n_in_hide_include_einvoice`: `Boolean` (compute `_compute_l10n_in_hide_include_einvoice`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_l10n_in_hide_include_einvoice`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_in_edi_gstr/Models]]

<!-- GENERATED:MODEL -->
