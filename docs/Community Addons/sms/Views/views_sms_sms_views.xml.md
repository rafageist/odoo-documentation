<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/sms_sms_views.xml

- Module: [[docs/Community Addons/sms/sms|sms]]
- Scope: Community Addons
- Source file: `views/sms_sms_views.xml`
- Views: 3
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `sms_sms_view_search`
- Name: sms.sms.view.search
- Model: `sms.sms`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `number`, `partner_id`
- XPath or positional patches: 0

### `sms_sms_view_tree`
- Name: sms.sms.view.list
- Model: `sms.sms`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `failure_type`, `number`, `partner_id`, `state`
- Buttons: `action_set_canceled`, `action_set_outgoing`, `send`
- XPath or positional patches: 0

### `sms_tsms_view_form`
- Name: sms.sms.view.form
- Model: `sms.sms`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `body`, `failure_type`, `mail_message_id`, `number`, `partner_id`, `state`, `to_delete`
- Buttons: `action_set_canceled`, `action_set_outgoing`, `send`
- XPath or positional patches: 0

## Actions

- `ir_actions_server_sms_sms_resend`: `server` Resend
- `sms_sms_action`: `act_window` SMS

## Menus

- `sms_sms_menu`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/sms/Views]]

<!-- GENERATED:VIEWFILE -->
