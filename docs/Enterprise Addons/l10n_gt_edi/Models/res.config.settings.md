<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/l10n_gt_edi/l10n_gt_edi|l10n_gt_edi]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Char` x 3, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_gt_edi_infile_key`: `Char` (related `company_id.l10n_gt_edi_infile_key`)
- `l10n_gt_edi_infile_token`: `Char` (related `company_id.l10n_gt_edi_infile_token`)
- `l10n_gt_edi_is_root_company`: `Boolean` (compute `_compute_l10n_gt_edi_is_root_company`)
- `l10n_gt_edi_service_provider`: `Selection` (related `company_id.l10n_gt_edi_service_provider`)
- `l10n_gt_edi_ws_prefix`: `Char` (related `company_id.l10n_gt_edi_ws_prefix`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_l10n_gt_edi_is_root_company`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_gt_edi/Models]]

<!-- GENERATED:MODEL -->
