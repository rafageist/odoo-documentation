<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteProfile

- Module: [[docs/Community Addons/website_profile/website_profile|website_profile]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 8

## Routes

### `get_user_profile_avatar`
- Paths: `/profile/avatar/<int:user_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `view_user_profile`
- Paths: `/profile/user/<int:user_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `save_edited_profile`
- Paths: `/profile/user/save`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `view_ranks_badges`
- Paths: `/profile/ranks_badges`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `view_all_users_page`
- Paths: `/profile/users`, `/profile/users/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `send_validation_email`
- Paths: `/profile/send_validation_email`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `validate_email`
- Paths: `/profile/validate_email`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `validate_email_done`
- Paths: `/profile/validate_email/close`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website_profile/Controllers]]

<!-- GENERATED:CONTROLLER -->
