---
tags: [odoo, enterprise, generated, views]
---

# views/frontdesk_frontdesk_views.xml

- Module: [[docs/Enterprise Addons/frontdesk/frontdesk|frontdesk]]
- Scope: Enterprise Addons
- Source file: `views/frontdesk_frontdesk_views.xml`
- Views: 4
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `frontdesk_frontdesk_view_search`
- Name: frontdesk.frontdesk.view.search
- Model: `frontdesk.frontdesk`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `responsible_ids`
- XPath or positional patches: 0

### `frontdesk_frontdesk_view_kanban`
- Name: frontdesk.frontdesk.view.kanban
- Model: `frontdesk.frontdesk`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `drink_to_serve`, `guest_on_site`, `is_favorite`, `latest_check_in`, `name`, `pending`, `responsible_ids`
- Buttons: `action_open_kiosk`
- XPath or positional patches: 0

### `frontdesk_frontdesk_view_tree`
- Name: frontdesk.frontdesk.view.list
- Model: `frontdesk.frontdesk`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `company_id`, `drink_offer`, `name`, `notify_discuss`, `notify_email`, `notify_sms`, `responsible_ids`, `self_check_in`
- XPath or positional patches: 0

### `frontdesk_frontdesk_view_form`
- Name: frontdesk.frontdesk.view.form
- Model: `frontdesk.frontdesk`
- Type: inferred from arch
- Root tag: `form`
- Field references: 23
- Sample fields: `access_token`, `active`, `ask_company`, `ask_email`, `ask_phone`, `authenticate_guest`, `company_id`, `description`, `drink_ids`, `drink_offer`, and 13 more
- Buttons: `%(frontdesk.action_frontdesk_drink)d`, `%(frontdesk_action_install_kiosk_pwa)d`
- XPath or positional patches: 0

## Actions

- `action_frontdesk_frontdesk_tree`: `act_window` Stations
- `action_frontdesk_frontdesk`: `act_window` Stations
- `frontdesk_action_install_kiosk_pwa`: `client` Frontdesk

## Navigation

- **Parent:** [[docs/Enterprise Addons/frontdesk/Views]]

