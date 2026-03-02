<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# PaymentPortal

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `controllers/portal.py`
- Base classes: `payment_portal.PaymentPortal`
- Routes: 4

## Routes

### `subscription_transaction`
- Paths: `/my/subscriptions/<int:order_id>/transaction`
- Type: `jsonrpc`
- Auth: `public`

### `subscription_transaction_from_invoice`
- Paths: `/my/subscriptions/invoice/<int:invoice_id>/transaction`
- Type: `jsonrpc`
- Auth: `public`

### `subscription_assign_token`
- Paths: `/my/subscriptions/assign_token/<int:order_id>`
- Type: `jsonrpc`
- Auth: `user`

### `payment_method`
- Paths: `<dynamic>`

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Controllers]]

<!-- GENERATED:CONTROLLER -->
