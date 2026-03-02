<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# digest.digest

- Module: [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/digest.py`
- Python classes: `DigestDigest`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 3, `Float` x 2, `Integer` x 1
- Relation fields: 0

## Sample fields

- `kpi_livechat_conversations`: `Boolean` (comodel `Conversations handled`)
- `kpi_livechat_conversations_value`: `Integer` (compute `_compute_kpi_livechat_conversations_value`)
- `kpi_livechat_rating`: `Boolean` (comodel `% of Happiness`)
- `kpi_livechat_rating_value`: `Float` (compute `_compute_kpi_livechat_rating_value`)
- `kpi_livechat_response`: `Boolean` (comodel `Time to answer (sec)`)
- `kpi_livechat_response_value`: `Float` (compute `_compute_kpi_livechat_response_value`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_kpi_livechat_conversations_value`, `_compute_kpi_livechat_rating_value`, `_compute_kpi_livechat_response_value`, `_compute_kpis_actions`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/im_livechat/Models]]

<!-- GENERATED:MODEL -->
