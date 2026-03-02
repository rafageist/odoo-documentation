<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# CustomerPortal

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `controllers/portal.py`
- Base classes: `payment_portal.PaymentPortal`
- Routes: 12

## Routes

### `my_subscription`
- Paths: `/my/subscription`, `/my/subscriptions`, `/my/subscriptions/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_quotes`
- Paths: `<dynamic>`

### `portal_my_orders`
- Paths: `<dynamic>`

### `subscription`
- Paths: `/my/subscription/<int:order_id>`, `/my/subscription/<int:order_id>/<access_token>`, `/my/subscriptions/<int:order_id>`, `/my/subscriptions/<int:order_id>/<access_token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `portal_quote_document`
- Paths: `/my/orders/<int:order_id>/document/<int:document_id>`, `/my/subscriptions/<int:order_id>/document/<int:document_id>`

### `close_account`
- Paths: `/my/subscription/<int:order_id>/close`, `/my/subscriptions/<int:order_id>/close`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `change_plan`
- Paths: `/my/subscriptions/<int:order_id>/change_plan`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `subscription_pause`
- Paths: `/my/subscriptions/<int:order_id>/pause`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `subscription_resume`
- Paths: `/my/subscriptions/<int:order_id>/resume`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `subscription_portal_upsell`
- Paths: `/my/subscriptions/<int:order_id>/upsell`
- Type: `http`
- Auth: `public`

### `subscription_portal_renewal`
- Paths: `/my/subscriptions/<int:order_id>/renewal`
- Type: `http`
- Auth: `public`

### `subscription_change_address`
- Paths: `/my/subscriptions/<int:order_id>/change_address`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Controllers]]

<!-- GENERATED:CONTROLLER -->
