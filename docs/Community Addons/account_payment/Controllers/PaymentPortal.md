<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# PaymentPortal

- Module: [[docs/Community Addons/account_payment/account_payment|account_payment]]
- Scope: Community Addons
- Source file: `controllers/payment.py`
- Base classes: `payment_portal.PaymentPortal`
- Routes: 3

## Routes

### `invoice_transaction`
- Paths: `/invoice/transaction/<int:invoice_id>`
- Type: `jsonrpc`
- Auth: `public`

### `overdue_invoices_transaction`
- Paths: `/invoice/transaction/overdue`
- Type: `jsonrpc`
- Auth: `public`

### `payment_pay`
- Paths: `<dynamic>`

## Navigation

- **Parent:** [[docs/Community Addons/account_payment/Controllers]]

<!-- GENERATED:CONTROLLER -->
