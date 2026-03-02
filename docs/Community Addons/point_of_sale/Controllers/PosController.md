<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# PosController

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `PortalAccount`
- Routes: 7

## Routes

### `pos_web_service_worker`
- Paths: `/pos/service-worker.js`
- Type: `http`
- Auth: `user`

### `old_pos_web`
- Paths: `/pos/ui`, `/pos/web`
- Type: `http`
- Auth: `user`

### `pos_web`
- Paths: `/pos/ui/<config_id>`, `/pos/ui/<config_id>/<path:subpath>`
- Type: `http`
- Auth: `user`

### `pos_ping`
- Paths: `/pos/ping`
- Type: `jsonrpc`
- Auth: `user`

### `print_sale_details`
- Paths: `/pos/sale_details_report`
- Type: `http`
- Auth: `user`

### `invoice_request_screen`
- Paths: `/pos/ticket`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `show_ticket_validation_screen`
- Paths: `/pos/ticket/validate`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Controllers]]

<!-- GENERATED:CONTROLLER -->
