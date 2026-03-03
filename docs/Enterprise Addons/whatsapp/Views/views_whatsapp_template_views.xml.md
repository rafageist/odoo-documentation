---
tags: [odoo, enterprise, generated, views]
---

# views/whatsapp_template_views.xml

- Module: [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]
- Scope: Enterprise Addons
- Source file: `views/whatsapp_template_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `whatsapp_template_view_search`
- Name: whatsapp.template.view.search
- Model: `whatsapp.template`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `body`, `model`, `model_id`, `name`
- XPath or positional patches: 0

### `whatsapp_template_view_kanban`
- Name: whatsapp.template.view.kanban
- Model: `whatsapp.template`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `allowed_user_ids`, `create_date`, `messages_count`, `model_id`, `name`, `quality`, `status`
- XPath or positional patches: 0

### `whatsapp_template_view_tree`
- Name: whatsapp.template.view.list
- Model: `whatsapp.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `create_date`, `create_uid`, `header_type`, `model_id`, `name`, `quality`, `sequence`, `status`, `template_name`, `wa_account_id`
- XPath or positional patches: 0

### `whatsapp_template_view_form`
- Name: whatsapp.template.view.form
- Model: `whatsapp.template`
- Type: inferred from arch
- Root tag: `form`
- Field references: 34
- Sample fields: `active`, `allowed_user_ids`, `body`, `button_ids`, `button_type`, `call_number`, `demo_value`, `display_name`, `field_name`, `field_type`, and 24 more
- Buttons: `%(whatsapp_preview_action_from_template)d`, `action_open_messages`, `button_create_action`, `button_delete_action`, `button_reset_to_draft`, `button_submit_template`, `button_sync_template`
- XPath or positional patches: 0

## Actions

- `whatsapp_template_action`: `act_window` WhatsApp Template

## Navigation

- **Parent:** [[docs/Enterprise Addons/whatsapp/Views]]

