<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.move

- Module: [[docs/Community Addons/account_peppol/account_peppol|account_peppol]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/account_move.py`
- Python classes: `AccountMove`

## Field footprint

- Detected fields: 2
- Field types: `Char` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `peppol_message_uuid`: `Char`
- `peppol_move_state`: `Selection` (compute `_compute_peppol_move_state`, store `True`)

## Method hints

- Detected methods: 5
- Action methods: `action_cancel_peppol_documents`, `action_send_and_print`
- Compute methods: `_compute_display_send_button`, `_compute_peppol_move_state`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/account_peppol/Models]]

<!-- GENERATED:MODEL -->
