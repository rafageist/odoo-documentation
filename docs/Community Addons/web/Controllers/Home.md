<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# Home

- Module: [[docs/Community Addons/web/web|web]]
- Scope: Community Addons
- Source file: `controllers/home.py`
- Base classes: `http.Controller`
- Routes: 8

## Routes

### `index`
- Paths: `/`
- Type: `http`
- Auth: `none`

### `web_client`
- Paths: `/odoo`, `/odoo/<path:subpath>`, `/scoped_app/<path:subpath>`, `/web`
- Type: `http`
- Auth: `none`
- Readonly: `_web_client_readonly`

### `web_load_menus`
- Paths: `/web/webclient/load_menus`
- Type: `http`
- Auth: `user`
- Readonly: `True`

### `web_login`
- Paths: `/web/login`
- Type: `http`
- Auth: `none`
- Readonly: `False`

### `login_successful_external_user`
- Paths: `/web/login_successful`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `switch_to_admin`
- Paths: `/web/become`
- Type: `http`
- Auth: `user`
- Readonly: `True`

### `health`
- Paths: `/web/health`
- Type: `http`
- Auth: `none`

### `robots`
- Paths: `/robots.txt`
- Type: `http`
- Auth: `none`

## Navigation

- **Parent:** [[docs/Community Addons/web/Controllers]]

<!-- GENERATED:CONTROLLER -->
