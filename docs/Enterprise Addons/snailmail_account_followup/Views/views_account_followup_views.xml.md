---
tags: [odoo, enterprise, generated, views]
---

# views/account_followup_views.xml

- Module: [[docs/Enterprise Addons/snailmail_account_followup/snailmail_account_followup|snailmail_account_followup]]
- Scope: Enterprise Addons
- Source file: `views/account_followup_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_followup_followup_line_form_inherit_snailmail`
- Name: account_followup.followup.line.form.inherit.snailmail
- Model: `account_followup.followup.line`
- Type: inferred from arch
- Inherits: `account_followup.view_account_followup_followup_line_form`
- Root tag: `field`
- Field references: 4
- Sample fields: `join_invoices`, `mail_template_id`, `send_letter`, `send_sms`
- XPath or positional patches: 0

### `view_account_followup_followup_line_tree_inherit_snailmail`
- Name: account_followup.followup.line.list.inherit.snailmail
- Model: `account_followup.followup.line`
- Type: inferred from arch
- Inherits: `account_followup.view_account_followup_followup_line_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `send_letter`, `send_sms`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/snailmail_account_followup/Views]]

