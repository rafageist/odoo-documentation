---
tags: [odoo, enterprise, generated, views]
---

# views/account_bank_statement_view.xml

- Module: [[docs/Enterprise Addons/account_online_synchronization/account_online_synchronization|account_online_synchronization]]
- Scope: Enterprise Addons
- Source file: `views/account_bank_statement_view.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_bank_statement_line_search_bank_rec_widget_inherit`
- Name: account.bank.statement.line.search.bank_rec_widget
- Model: `account.bank.statement.line`
- Type: inferred from arch
- Inherits: `account_accountant.view_bank_statement_line_search_bank_rec_widget`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_bank_statement_line_form_bank_rec_widget_inherit`
- Name: account.bank.statement.line.form.bank_rec_widget.inherit
- Model: `account.bank.statement.line`
- Type: inferred from arch
- Inherits: `account_accountant.view_bank_statement_line_form_bank_rec_widget`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_bank_statement_line_tree_inherit`
- Name: bank.statement.line.list.inherit
- Model: `account.bank.statement.line`
- Type: inferred from arch
- Inherits: `account_accountant.view_bank_statement_line_tree_bank_rec_widget`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `online_account_id`, `online_link_id`, `online_transaction_identifier`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_online_synchronization/Views]]

