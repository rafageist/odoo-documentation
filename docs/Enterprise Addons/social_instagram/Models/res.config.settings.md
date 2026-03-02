<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/social_instagram/social_instagram|social_instagram]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 2
- Relation fields: 0

## Sample fields

- `instagram_app_id`: `Char` (comodel `Instagram App ID`, compute `_compute_instagram_app_id`)
- `instagram_client_secret`: `Char` (comodel `Instagram App Secret`, compute `_compute_instagram_client_secret`)
- `instagram_use_own_account`: `Boolean` (comodel `Use your own Instagram Account`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_instagram_app_id`, `_compute_instagram_client_secret`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_instagram/Models]]

<!-- GENERATED:MODEL -->
