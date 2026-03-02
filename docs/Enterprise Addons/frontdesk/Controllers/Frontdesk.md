<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# Frontdesk

- Module: [[docs/Enterprise Addons/frontdesk/frontdesk|frontdesk]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 11

## Routes

### `launch_frontdesk`
- Paths: `/kiosk/<int:frontdesk_id>/<string:token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `launch_frontdesk_mobile`
- Paths: `/kiosk/<int:frontdesk_id>/mobile/<string:token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `get_tmp_code`
- Paths: `/kiosk/<int:frontdesk_id>/get_tmp_code/<string:token>`
- Type: `jsonrpc`
- Auth: `public`

### `get_frontdesk_data`
- Paths: `/frontdesk/<int:frontdesk_id>/<string:token>/get_frontdesk_data`
- Type: `jsonrpc`
- Auth: `public`

### `get_planned_visitors`
- Paths: `/frontdesk/<int:frontdesk_id>/<string:token>/get_planned_visitors`
- Type: `jsonrpc`
- Auth: `public`

### `frontdesk_background_image`
- Paths: `/frontdesk/<int:frontdesk_id>/background`
- Type: `http`
- Auth: `public`

### `get_frontdesk_drinks`
- Paths: `/frontdesk/<int:drink_id>/get_frontdesk_drinks`
- Type: `http`
- Auth: `public`

### `hosts_infos`
- Paths: `/frontdesk/<int:frontdesk_id>/<string:token>/hosts_infos`
- Type: `jsonrpc`
- Auth: `public`

### `get_departments`
- Paths: `/frontdesk/<int:frontdesk_id>/<string:token>/get_departments`
- Type: `jsonrpc`
- Auth: `public`

### `prepare_visitor_data`
- Paths: `/frontdesk/<int:frontdesk_id>/<string:token>/prepare_visitor_data`
- Type: `jsonrpc`
- Auth: `public`

### `frontdesk_visitor_check_out`
- Paths: `/frontdesk/visitor/check_out/<int:visitor_id>`
- Type: `http`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Enterprise Addons/frontdesk/Controllers]]

<!-- GENERATED:CONTROLLER -->
