<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# CustomerPortal

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `controllers/portal.py`
- Base classes: `payment_portal.PaymentPortal`
- Routes: 7

## Routes

### `portal_my_quotes`
- Paths: `/my/quotes`, `/my/quotes/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_orders`
- Paths: `/my/orders`, `/my/orders/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_order_page`
- Paths: `/my/orders/<int:order_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `portal_quote_accept`
- Paths: `/my/orders/<int:order_id>/accept`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `portal_quote_decline`
- Paths: `/my/orders/<int:order_id>/decline`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `portal_quote_document`
- Paths: `/my/orders/<int:order_id>/document/<int:document_id>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `portal_my_sale_order_download_edi`
- Paths: `/my/orders/<int:order_id>/download_edi`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/sale/Controllers]]

<!-- GENERATED:CONTROLLER -->
