<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/discuss_channel_views.xml

- Module: [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]
- Scope: Enterprise Addons
- Source file: `views/discuss_channel_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `discuss_channel_view_list_whatsapp`
- Name: discuss.channel.view.list.whatsapp
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `channel_partner_ids`, `create_date`, `name`, `whatsapp_channel_active`
- XPath or positional patches: 0

### `discuss_channel_view_form`
- Name: discuss.channel.view.form.inherit.whatsapp
- Model: `discuss.channel`
- Type: inferred from arch
- Inherits: `mail.discuss_channel_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `last_wa_mail_message_id`, `wa_account_id`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/whatsapp/Views]]

<!-- GENERATED:VIEWFILE -->
