<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteBackend

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Source file: `controllers/backend.py`
- Base classes: `http.Controller`
- Routes: 4

## Routes

### `fetch_dashboard_data`
- Paths: `/website/fetch_dashboard_data`
- Type: `jsonrpc`
- Auth: `user`
- Readonly: `True`

### `get_iframe_fallback`
- Paths: `/website/iframefallback`
- Type: `http`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `check_create_access_rights`
- Paths: `/website/check_new_content_access_rights`
- Type: `jsonrpc`
- Auth: `user`
- Readonly: `True`

### `website_track_installing_modules`
- Paths: `/website/track_installing_modules`
- Type: `jsonrpc`
- Auth: `user`
- Readonly: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website/Controllers]]

<!-- GENERATED:CONTROLLER -->
