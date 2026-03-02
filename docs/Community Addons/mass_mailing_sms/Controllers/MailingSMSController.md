<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# MailingSMSController

- Module: [[docs/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 3

## Routes

### `blacklist_page`
- Paths: `/sms/<int:mailing_id>/<string:trace_code>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `blacklist_number`
- Paths: `/sms/<int:mailing_id>/unsubscribe/<string:trace_code>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `sms_short_link_redirect`
- Paths: `/r/<string:code>/s/<int:sms_id_int>`
- Type: `http`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing_sms/Controllers]]

<!-- GENERATED:CONTROLLER -->
