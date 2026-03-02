<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.partner

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_partner.py`
- Python classes: `ResPartner`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 1, `Integer` x 1
- Relation fields: 0

## Sample fields

- `event_count`: `Integer` (comodel `# Events`, compute `_compute_event_count`)
- `static_map_url`: `Char` (compute `_compute_static_map_url`)
- `static_map_url_is_valid`: `Boolean` (compute `_compute_static_map_url_is_valid`)

## Method hints

- Detected methods: 5
- Action methods: `action_event_view`
- Compute methods: `_compute_event_count`, `_compute_static_map_url`, `_compute_static_map_url_is_valid`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/event/Models]]

<!-- GENERATED:MODEL -->
