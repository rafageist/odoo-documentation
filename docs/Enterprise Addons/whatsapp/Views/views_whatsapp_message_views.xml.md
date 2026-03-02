<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/whatsapp_message_views.xml

- Module: [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]
- Scope: Enterprise Addons
- Source file: `views/whatsapp_message_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `whatsapp_message_view_search`
- Name: whatsapp.message.view.search
- Model: `whatsapp.message`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `body`, `create_date`, `mobile_number`, `state`
- XPath or positional patches: 0

### `whatsapp_message_view_form`
- Name: whatsapp.message.view.form
- Model: `whatsapp.message`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `body`, `create_date`, `failure_reason`, `failure_type`, `free_text_json`, `mail_message_id`, `mobile_number`, `msg_uid`, `state`, `wa_template_id`
- Buttons: `button_cancel_send`
- XPath or positional patches: 0

### `whatsapp_message_view_graph`
- Name: whatsapp.message.view.graph
- Model: `whatsapp.message`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `create_date`, `state`
- XPath or positional patches: 0

### `whatsapp_message_view_tree`
- Name: whatsapp.message.view.list
- Model: `whatsapp.message`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `body`, `create_date`, `create_uid`, `failure_reason`, `failure_type`, `mobile_number`, `state`, `wa_template_id`
- Buttons: `button_cancel_send`, `button_resend`
- XPath or positional patches: 0

## Actions

- `whatsapp_message_action`: `act_window` WhatsApp Messages

## Navigation

- **Parent:** [[docs/Enterprise Addons/whatsapp/Views]]

<!-- GENERATED:VIEWFILE -->
