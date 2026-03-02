<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# CustomerPortal

- Module: [[docs/Community Addons/portal/portal|portal]]
- Scope: Community Addons
- Source file: `controllers/portal.py`
- Base classes: `Controller`
- Routes: 11

## Routes

### `counters`
- Paths: `/my/counters`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `home`
- Paths: `/my`, `/my/home`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `account`
- Paths: `/my/account`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `my_addresses`
- Paths: `/my/addresses`
- Type: `http`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `portal_address`
- Paths: `/my/address`
- Type: `http`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `portal_address_submit`
- Paths: `/my/address/submit`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_address_country_info`
- Paths: `/my/address/country_info/<model("res.country"):country>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `address_archive`
- Paths: `/my/address/archive`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `security`
- Paths: `/my/security`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `deactivate_account`
- Paths: `/my/deactivate_account`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `attachment_remove`
- Paths: `/portal/attachment/remove`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/portal/Controllers]]

<!-- GENERATED:CONTROLLER -->
