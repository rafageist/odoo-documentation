<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebJson2Controller

- Module: [[docs/Community Addons/rpc/rpc|rpc]]
- Scope: Community Addons
- Source file: `controllers/json2.py`
- Base classes: `http.Controller`
- Routes: 2

## Routes

### `web_json_2_404`
- Paths: `/json/2`, `/json/2/<path:subpath>`
- Type: `json2`
- Auth: `public`
- Readonly: `True`

### `web_json_2_rpc`
- Paths: `/json/2/<model>/<method>`
- Type: `json2`
- Auth: `bearer`
- Readonly: `_web_json_2_rpc_readonly`

## Navigation

- **Parent:** [[docs/Community Addons/rpc/Controllers]]

<!-- GENERATED:CONTROLLER -->
