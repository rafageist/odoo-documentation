<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# CustomerPortal

- Module: [[docs/Community Addons/purchase/purchase|purchase]]
- Scope: Community Addons
- Source file: `controllers/portal.py`
- Base classes: `portal.CustomerPortal`
- Routes: 5

## Routes

### `portal_my_requests_for_quotation`
- Paths: `/my/rfq`, `/my/rfq/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_purchase_orders`
- Paths: `/my/purchase`, `/my/purchase/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_purchase_order`
- Paths: `/my/purchase/<int:order_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `portal_my_purchase_order_update_dates`
- Paths: `/my/purchase/<int:order_id>/update`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `portal_my_purchase_order_download_edi`
- Paths: `/my/purchase/<int:order_id>/download_edi`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/purchase/Controllers]]

<!-- GENERATED:CONTROLLER -->
