<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/social_youtube/social_youtube|social_youtube]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 2
- Relation fields: 0

## Sample fields

- `youtube_oauth_client_id`: `Char` (comodel `YouTube OAuth Client ID`, compute `_compute_youtube_oauth_client_id`)
- `youtube_oauth_client_secret`: `Char` (comodel `YouTube OAuth Client Secret`, compute `_compute_youtube_oauth_client_secret`)
- `youtube_use_own_account`: `Boolean` (comodel `Use your own YouTube Account`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_youtube_oauth_client_id`, `_compute_youtube_oauth_client_secret`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_youtube/Models]]

<!-- GENERATED:MODEL -->
