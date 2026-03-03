---
tags: [odoo, enterprise, generated, views]
---

# views/account_journal_view.xml

- Module: [[docs/Enterprise Addons/account_online_synchronization/account_online_synchronization|account_online_synchronization]]
- Scope: Enterprise Addons
- Source file: `views/account_journal_view.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `account_journal_form`
- Name: account.journal.form.online.sync
- Model: `account.journal`
- Type: inferred from arch
- Inherits: `account.view_account_journal_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `account_online_account_id`, `renewal_contact_email`
- Buttons: `action_send_reminder`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_online_synchronization/Views]]

