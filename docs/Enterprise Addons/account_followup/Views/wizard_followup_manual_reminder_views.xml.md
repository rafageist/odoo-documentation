---
tags: [odoo, enterprise, generated, views]
---

# wizard/followup_manual_reminder_views.xml

- Module: [[docs/Enterprise Addons/account_followup/account_followup|account_followup]]
- Scope: Enterprise Addons
- Source file: `wizard/followup_manual_reminder_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `manual_reminder_view_form`
- Name: account.followup.manual_reminder.view.form
- Model: `account_followup.manual_reminder`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `attachment_ids`, `body`, `can_edit_body`, `email`, `email_recipient_ids`, `join_invoices`, `lang`, `print`, `render_model`, `sms`, and 4 more
- Buttons: `process_followup`
- XPath or positional patches: 0

## Actions

- `manual_reminder_action`: `act_window` Send and Print

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_followup/Views]]

