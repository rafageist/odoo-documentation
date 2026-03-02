<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# PaymentPortal

- Module: [[docs/Community Addons/website_payment/website_payment|website_payment]]
- Scope: Community Addons
- Source file: `controllers/portal.py`
- Base classes: `payment_portal.PaymentPortal`
- Routes: 3

## Routes

### `donation_pay`
- Paths: `/donation/pay`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `donation_transaction`
- Paths: `/donation/transaction/<minimum_amount>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `get_supported_payment_methods`
- Paths: `/website_payment/snippet/supported_payment_methods`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website_payment/Controllers]]

<!-- GENERATED:CONTROLLER -->

