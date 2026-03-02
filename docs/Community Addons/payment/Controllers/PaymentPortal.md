<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# PaymentPortal

- Module: [[docs/Community Addons/payment/payment|payment]]
- Scope: Community Addons
- Source file: `controllers/portal.py`
- Base classes: `portal.CustomerPortal`
- Routes: 5

## Routes

### `payment_pay`
- Paths: `/payment/pay`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `payment_method`
- Paths: `/my/payment_method`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `payment_transaction`
- Paths: `/payment/transaction`
- Type: `jsonrpc`
- Auth: `public`

### `payment_confirm`
- Paths: `/payment/confirmation`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `archive_token`
- Paths: `/payment/archive_token`
- Type: `jsonrpc`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Community Addons/payment/Controllers]]

<!-- GENERATED:CONTROLLER -->
