<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# ir.actions.server

- Module: [[docs/Enterprise Addons/ai_server_actions/ai_server_actions|ai_server_actions]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/ir_actions_server.py`
- Python classes: `IrActionsServer`

## Field footprint

- Detected fields: 5
- Field types: `Char` x 2, `Html` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `ai_update_prompt`: `Html` (comodel `AI Update Prompt`)
- `evaluation_type`: `Selection`
- `update_field_name`: `Char` (related `update_field_id.name`)
- `update_field_relation`: `Char` (related `update_field_id.relation`)
- `update_field_type`: `Selection` (related `update_field_id.ttype`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/ai_server_actions/Models]]

<!-- GENERATED:MODEL -->
