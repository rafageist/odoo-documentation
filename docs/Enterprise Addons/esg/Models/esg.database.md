<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# esg.database

- Module: [[docs/Enterprise Addons/esg/esg|esg]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/esg_database.py`
- Python classes: `EsgDatabase`
- Description: Database

## Field footprint

- Detected fields: 8
- Field types: `Binary` x 1, `Boolean` x 1, `Char` x 3, `Date` x 2, `Integer` x 1
- Relation fields: 0

## Sample fields

- `can_be_downloaded`: `Boolean` (compute `_compute_can_be_downloaded`)
- `color`: `Integer` (compute `_compute_kanban_display`)
- `image`: `Binary`
- `kanban_text`: `Char` (compute `_compute_kanban_display`)
- `last_update`: `Date`
- `latest_version`: `Date`
- `name`: `Char`
- `url`: `Char`

## Method hints

- Detected methods: 9
- Action methods: `action_load_data`
- Compute methods: `_compute_can_be_downloaded`, `_compute_kanban_display`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg/Models]]

<!-- GENERATED:MODEL -->
