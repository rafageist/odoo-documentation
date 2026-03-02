<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# ir.actions.server

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/ir_actions_server.py`
- Python classes: `IrActionsServer`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 1, `Char` x 3
- Relation fields: 0

## Sample fields

- `website_path`: `Char` (comodel `Website Path`)
- `website_published`: `Boolean` (comodel `Available on the Website`)
- `website_url`: `Char` (comodel `Website Url`, compute `_get_website_url`)
- `xml_id`: `Char` (comodel `External ID`, compute `_compute_xml_id`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_website_url`, `_compute_xml_id`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/website/Models]]

<!-- GENERATED:MODEL -->
