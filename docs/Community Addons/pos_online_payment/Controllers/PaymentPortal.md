<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# PaymentPortal

- Module: [[docs/Community Addons/pos_online_payment/pos_online_payment|pos_online_payment]]
- Scope: Community Addons
- Source file: `controllers/payment_portal.py`
- Base classes: `payment_portal.PaymentPortal`
- Routes: 3

## Routes

### `pos_order_pay`
- Paths: `/pos/pay/<int:pos_order_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `pos_order_pay_transaction`
- Paths: `/pos/pay/transaction/<int:pos_order_id>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `pos_order_pay_confirmation`
- Paths: `/pos/pay/confirmation/<int:pos_order_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/pos_online_payment/Controllers]]

<!-- GENERATED:CONTROLLER -->
