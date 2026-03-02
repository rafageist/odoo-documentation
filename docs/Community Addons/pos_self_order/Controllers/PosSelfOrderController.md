<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# PosSelfOrderController

- Module: [[docs/Community Addons/pos_self_order/pos_self_order|pos_self_order]]
- Scope: Community Addons
- Source file: `controllers/orders.py`
- Base classes: `http.Controller`
- Routes: 9

## Routes

### `process_order`
- Paths: `/pos-self-order/process-order/<device_type>/`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `validate_partner`
- Paths: `/pos-self-order/validate-partner`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `remove_order`
- Paths: `/pos-self-order/remove-order`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `get_orders_by_access_token`
- Paths: `/pos-self-order/get-user-data`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `pos_self_order_kiosk_payment`
- Paths: `/kiosk/payment/<int:pos_config_id>/<device_type>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `pos_kiosk_increment_nb_print`
- Paths: `/pos_self_order/kiosk/increment_nb_print/`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `change_printer_status`
- Paths: `/pos-self-order/change-printer-status`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `get_slots`
- Paths: `/pos-self-order/get-slots`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `pos_ping`
- Paths: `/pos-self/ping`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/pos_self_order/Controllers]]

<!-- GENERATED:CONTROLLER -->
