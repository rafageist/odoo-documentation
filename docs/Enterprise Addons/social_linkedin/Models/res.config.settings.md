<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/social_linkedin/social_linkedin|social_linkedin]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 2
- Relation fields: 0

## Sample fields

- `linkedin_app_id`: `Char` (comodel `App ID`, compute `_compute_linkedin_app_id`)
- `linkedin_client_secret`: `Char` (comodel `App Secret`, compute `_compute_linkedin_client_secret`)
- `linkedin_use_own_account`: `Boolean` (comodel `Use your own LinkedIn Account`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_linkedin_app_id`, `_compute_linkedin_client_secret`
- Onchange methods: `_onchange_linkedin_use_own_account`

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_linkedin/Models]]

<!-- GENERATED:MODEL -->
