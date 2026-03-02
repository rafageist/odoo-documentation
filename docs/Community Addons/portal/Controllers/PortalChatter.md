<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# PortalChatter

- Module: [[docs/Community Addons/portal/portal|portal]]
- Scope: Community Addons
- Source file: `controllers/portal_thread.py`
- Base classes: `ThreadController`
- Routes: 4

## Routes

### `portal_avatar`
- Paths: `/mail/avatar/mail.message/<int:res_id>/author_avatar/<int:width>x<int:height>`
- Type: `http`
- Auth: `public`

### `portal_chatter_init`
- Paths: `/portal/chatter_init`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `portal_message_fetch`
- Paths: `/mail/chatter_fetch`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `portal_message_update_is_internal`
- Paths: `/mail/update_is_internal`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/portal/Controllers]]

<!-- GENERATED:CONTROLLER -->
