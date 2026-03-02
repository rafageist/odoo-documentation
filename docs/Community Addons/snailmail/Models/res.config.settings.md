<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.config.settings

- Module: [[docs/Community Addons/snailmail/snailmail|snailmail]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 4
- Relation fields: 0

## Sample fields

- `snailmail_color`: `Boolean` (related `company_id.snailmail_color`)
- `snailmail_cover`: `Boolean` (related `company_id.snailmail_cover`)
- `snailmail_cover_readonly`: `Boolean` (compute `_compute_cover_readonly`)
- `snailmail_duplex`: `Boolean` (related `company_id.snailmail_duplex`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_cover_readonly`
- Onchange methods: `_onchange_layout`

## Navigation

- **Parent:** [[docs/Community Addons/snailmail/Models]]

<!-- GENERATED:MODEL -->
