---
tags: [odoo, enterprise, generated, views]
---

# wizard/batch_error_views.xml

- Module: [[docs/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]]
- Scope: Enterprise Addons
- Source file: `wizard/batch_error_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `batch_error_wizard_line_tree`
- Name: account.batch.error.wizard.line.list
- Model: `account.batch.error.wizard.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `description`, `help_message`, `show_remove_button`
- Buttons: `open_payments`, `remove_payments_from_batch`
- XPath or positional patches: 0

### `batch_error_wizard_form`
- Name: account.batch.error.wizard.form
- Model: `account.batch.error.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `error_line_ids`, `warning_line_ids`
- Buttons: `proceed_with_validation`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_batch_payment/Views]]

