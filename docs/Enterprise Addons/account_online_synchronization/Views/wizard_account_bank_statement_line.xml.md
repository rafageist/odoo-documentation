<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# wizard/account_bank_statement_line.xml

- Module: [[docs/Enterprise Addons/account_online_synchronization/account_online_synchronization|account_online_synchronization]]
- Scope: Enterprise Addons
- Source file: `wizard/account_bank_statement_line.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `missing_bank_statement_line_search`
- Name: missing.bank.statement.line.search
- Model: `account.bank.statement.line.transient`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `state`
- XPath or positional patches: 0

### `view_missing_bank_statement_line_tree`
- Name: missing.bank.statement.line.list
- Model: `account.bank.statement.line.transient`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `account_number`, `amount`, `amount_currency`, `date`, `online_transaction_identifier`, `partner_name`, `payment_ref`, `state`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_online_synchronization/Views]]

<!-- GENERATED:VIEWFILE -->
