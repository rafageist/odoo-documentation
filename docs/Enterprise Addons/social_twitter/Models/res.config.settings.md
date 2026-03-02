<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/social_twitter/social_twitter|social_twitter]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 2
- Relation fields: 0

## Sample fields

- `twitter_consumer_key`: `Char` (comodel `X Consumer Key`, compute `_compute_twitter_consumer_key`)
- `twitter_consumer_secret_key`: `Char` (comodel `X Consumer Secret Key`, compute `_compute_twitter_consumer_secret_key`)
- `twitter_use_own_account`: `Boolean` (comodel `Use your own X Account`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_twitter_consumer_key`, `_compute_twitter_consumer_secret_key`
- Onchange methods: `_onchange_twitter_use_own_account`

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_twitter/Models]]

<!-- GENERATED:MODEL -->
