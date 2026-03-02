<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# PosSelfKiosk

- Module: [[docs/Community Addons/pos_self_order/pos_self_order|pos_self_order]]
- Scope: Community Addons
- Source file: `controllers/self_entry.py`
- Base classes: `http.Controller`
- Routes: 3

## Routes

### `start_self_ordering`
- Paths: `/pos-self/<config_id>`, `/pos-self/<config_id>/<path:subpath>`
- Auth: `public`
- Website route: `True`

### `get_self_ordering_data`
- Paths: `/pos-self/data/<config_id>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `get_self_ordering_relations`
- Paths: `/pos-self/relations/<config_id>`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/pos_self_order/Controllers]]

<!-- GENERATED:CONTROLLER -->
