<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/social_facebook/social_facebook|social_facebook]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 2
- Relation fields: 0

## Sample fields

- `facebook_app_id`: `Char` (comodel `Facebook App ID`, compute `_compute_facebook_app_id`)
- `facebook_client_secret`: `Char` (comodel `Facebook App Secret`, compute `_compute_facebook_client_secret`)
- `facebook_use_own_account`: `Boolean` (comodel `Use your own Facebook Account`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_facebook_app_id`, `_compute_facebook_client_secret`
- Onchange methods: `_onchange_facebook_use_own_account`

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_facebook/Models]]

<!-- GENERATED:MODEL -->
