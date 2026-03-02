<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# IoTController

- Module: [[docs/Enterprise Addons/iot/iot|iot]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 8

## Routes

### `get_handlers`
- Paths: `/iot/get_handlers`
- Type: `http`
- Auth: `public`

### `load_keyboard_layouts`
- Paths: `/iot/keyboard_layouts`
- Type: `http`
- Auth: `public`

### `get_url`
- Paths: `/iot/box/<string:identifier>/display_url`
- Type: `http`
- Auth: `public`

### `iot_box_send_websocket`
- Paths: `/iot/box/send_websocket`
- Type: `jsonrpc`
- Auth: `public`

### `iot_box_webrtc_answer`
- Paths: `/iot/box/webrtc_answer`
- Type: `jsonrpc`
- Auth: `public`

### `update_box`
- Paths: `/iot/setup`
- Type: `jsonrpc`
- Auth: `public`

### `receive_iot_log`
- Paths: `/iot/log`
- Type: `http`
- Auth: `public`

### `update_certificate_status`
- Paths: `/iot/box/update_certificate_status`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Enterprise Addons/iot/Controllers]]

<!-- GENERATED:CONTROLLER -->
