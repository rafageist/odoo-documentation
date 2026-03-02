<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebClient

- Module: [[docs/Community Addons/web/web|web]]
- Scope: Community Addons
- Source file: `controllers/webclient.py`
- Base classes: `http.Controller`
- Routes: 6

## Routes

### `bootstrap_translations`
- Paths: `/web/webclient/bootstrap_translations`
- Type: `jsonrpc`
- Auth: `none`

### `translations`
- Paths: `/web/webclient/translations`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `version_info`
- Paths: `/web/webclient/version_info`
- Type: `jsonrpc`
- Auth: `none`

### `unit_tests_suite`
- Paths: `/web/tests`
- Type: `http`
- Auth: `user`
- Readonly: `True`

### `test_suite`
- Paths: `/web/tests/legacy`
- Type: `http`
- Auth: `user`
- Readonly: `True`

### `bundle`
- Paths: `/web/bundle/<string:bundle_name>`
- Auth: `public`
- Readonly: `True`

## Navigation

- **Parent:** [[docs/Community Addons/web/Controllers]]

<!-- GENERATED:CONTROLLER -->
