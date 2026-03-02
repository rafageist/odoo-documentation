<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/l10n_us_direct_deposit/l10n_us_direct_deposit|l10n_us_direct_deposit]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 3
- Field types: `Char` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `wise_api_key`: `Char` (related `company_id.wise_api_key`)
- `wise_environment`: `Selection` (related `company_id.wise_environment`)
- `wise_profile_identifier`: `Char` (related `company_id.wise_profile_identifier`)

## Method hints

- Detected methods: 3
- Action methods: `action_connect_wise`
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_us_direct_deposit/Models]]

<!-- GENERATED:MODEL -->
