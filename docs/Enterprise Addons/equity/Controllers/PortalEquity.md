<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# PortalEquity

- Module: [[docs/Enterprise Addons/equity/equity|equity]]
- Scope: Enterprise Addons
- Source file: `controllers/portal.py`
- Base classes: `CustomerPortal`
- Routes: 5

## Routes

### `portal_my_company_equity`
- Paths: `/my/equity/<int:partner_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `portal_my_equity`
- Paths: `/my/equity`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `portal_my_ubo`
- Paths: `/my/ubo`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `submit_ubo_form_data`
- Paths: `/my/ubo/submit/data`
- Type: `jsonrpc`
- Auth: `public`

### `portal_my_ubo_submit`
- Paths: `/my/ubo/submit`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Enterprise Addons/equity/Controllers]]

<!-- GENERATED:CONTROLLER -->
