<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.config.settings

- Module: [[docs/Community Addons/l10n_hu_edi/l10n_hu_edi|l10n_hu_edi]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 1, `Char` x 4, `Selection` x 2
- Relation fields: 0

## Sample fields

- `l10n_hu_edi_is_active`: `Boolean` (compute `_compute_l10n_hu_edi_is_active`)
- `l10n_hu_edi_password`: `Char` (related `company_id.l10n_hu_edi_password`)
- `l10n_hu_edi_replacement_key`: `Char` (related `company_id.l10n_hu_edi_replacement_key`)
- `l10n_hu_edi_server_mode`: `Selection` (related `company_id.l10n_hu_edi_server_mode`)
- `l10n_hu_edi_signature_key`: `Char` (related `company_id.l10n_hu_edi_signature_key`)
- `l10n_hu_edi_username`: `Char` (related `company_id.l10n_hu_edi_username`)
- `l10n_hu_tax_regime`: `Selection` (related `company_id.l10n_hu_tax_regime`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_l10n_hu_edi_is_active`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/l10n_hu_edi/Models]]

<!-- GENERATED:MODEL -->
