<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.config.settings

- Module: [[docs/Community Addons/cloud_storage_google/cloud_storage_google|cloud_storage_google]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 4
- Field types: `Binary` x 1, `Char` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `cloud_storage_google_account_info`: `Char` (compute `_compute_cloud_storage_google_account_info`, store `True`)
- `cloud_storage_google_bucket_name`: `Char`
- `cloud_storage_google_service_account_key`: `Binary` (store `False`)
- `cloud_storage_provider`: `Selection`

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_cloud_storage_google_account_info`
- Onchange methods: `_compute_cloud_storage_google_account_info`

## Navigation

- **Parent:** [[docs/Community Addons/cloud_storage_google/Models]]

<!-- GENERATED:MODEL -->
