<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# Session

- Module: [[docs/Community Addons/web/web|web]]
- Scope: Community Addons
- Source file: `controllers/session.py`
- Base classes: `http.Controller`
- Routes: 8

## Routes

### `get_session_info`
- Paths: `/web/session/get_session_info`
- Type: `jsonrpc`
- Auth: `user`
- Readonly: `True`

### `authenticate`
- Paths: `/web/session/authenticate`
- Type: `jsonrpc`
- Auth: `none`
- Readonly: `False`

### `get_lang_list`
- Paths: `/web/session/get_lang_list`
- Type: `jsonrpc`
- Auth: `none`

### `modules`
- Paths: `/web/session/modules`
- Type: `jsonrpc`
- Auth: `user`
- Readonly: `True`

### `check`
- Paths: `/web/session/check`
- Type: `jsonrpc`
- Auth: `user`
- Readonly: `True`

### `account`
- Paths: `/web/session/account`
- Type: `jsonrpc`
- Auth: `user`
- Readonly: `True`

### `destroy`
- Paths: `/web/session/destroy`
- Type: `jsonrpc`
- Auth: `user`
- Readonly: `True`

### `logout`
- Paths: `/web/session/logout`
- Type: `http`
- Auth: `none`
- Readonly: `True`

## Navigation

- **Parent:** [[docs/Community Addons/web/Controllers]]

<!-- GENERATED:CONTROLLER -->
