---
tags: [odoo, enterprise, generated, views]
---

# views/account_followup_line_views.xml

- Module: [[docs/Enterprise Addons/whatsapp_account_followup/whatsapp_account_followup|whatsapp_account_followup]]
- Scope: Enterprise Addons
- Source file: `views/account_followup_line_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_followup_followup_line_form_inherit_whatsapp`
- Name: account_followup.followup.line.form.inherit.whatsapp
- Model: `account_followup.followup.line`
- Type: inferred from arch
- Inherits: `account_followup.view_account_followup_followup_line_form`
- Root tag: `field`
- Field references: 4
- Sample fields: `mail_template_id`, `send_email`, `send_whatsapp`, `whatsapp_template_id`
- XPath or positional patches: 0

### `view_account_followup_followup_line_tree_inherit_whatsapp`
- Name: account_followup.followup.line.list.inherit.whatsapp
- Model: `account_followup.followup.line`
- Type: inferred from arch
- Inherits: `account_followup.view_account_followup_followup_line_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `send_email`, `send_whatsapp`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/whatsapp_account_followup/Views]]

