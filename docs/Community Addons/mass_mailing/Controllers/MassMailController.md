<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# MassMailController

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 16

## Routes

### `mailing_my`
- Paths: `/mailing/my`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `mailing_unsubscribe_oneclick`
- Paths: `/mailing/<int:mailing_id>/unsubscribe_oneclick`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `mailing_confirm_unsubscribe`
- Paths: `/mailing/<int:mailing_id>/confirm_unsubscribe`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `mailing_confirm_unsubscribe_post`
- Paths: `/mailing/confirm_unsubscribe`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `mailing_unsubscribe`
- Paths: `/mailing/<int:mailing_id>/unsubscribe`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `mailing_update_list_subscription`
- Paths: `/mailing/list/update`
- Type: `jsonrpc`
- Auth: `public`

### `mailing_send_feedback`
- Paths: `/mailing/feedback`
- Type: `jsonrpc`
- Auth: `public`

### `mailing_unsubscribe_placeholder_link`
- Paths: `/unsubscribe_from_list`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `mailing_view_in_browser_placeholder_link`
- Paths: `/view`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `track_mail_open`
- Paths: `/mail/track/<int:mail_id>/<string:token>/blank.gif`
- Type: `http`
- Auth: `public`

### `full_url_redirect`
- Paths: `/r/<string:code>/m/<int:mailing_trace_id>`
- Type: `http`
- Auth: `public`

### `mailing_report_deactivate`
- Paths: `/mailing/report/unsubscribe`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `mailing_view_in_browser`
- Paths: `/mailing/<int:mailing_id>/view`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `mail_blocklist_add`
- Paths: `/mailing/blocklist/add`
- Type: `jsonrpc`
- Auth: `public`

### `mail_blocklist_remove`
- Paths: `/mailing/blocklist/remove`
- Type: `jsonrpc`
- Auth: `public`

### `mass_mailing_preview_mobile_content`
- Paths: `/mailing/mobile/preview`
- Type: `http`
- Auth: `user`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Controllers]]

<!-- GENERATED:CONTROLLER -->
