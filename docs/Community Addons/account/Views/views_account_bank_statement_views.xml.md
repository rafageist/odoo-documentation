<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_bank_statement_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/account_bank_statement_views.xml`
- Views: 4
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `account_bank_statement_graph`
- Name: account.bank.statement.graph
- Model: `account.bank.statement`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `balance_end`, `balance_start`, `date`
- XPath or positional patches: 0

### `account_bank_statement_pivot`
- Name: account.bank.statement.pivot
- Model: `account.bank.statement`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `balance_end`, `balance_start`, `date`
- XPath or positional patches: 0

### `view_bank_statement_search`
- Name: account.bank.statement.search
- Model: `account.bank.statement`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `date`, `journal_id`, `name`
- XPath or positional patches: 0

### `view_bank_statement_tree`
- Name: account.bank.statement.list
- Model: `account.bank.statement`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `balance_end`, `balance_end_real`, `balance_start`, `company_id`, `currency_id`, `date`, `is_complete`, `is_valid`, `journal_id`, `name`
- XPath or positional patches: 0

## Actions

- `action_view_bank_statement_tree`: `act_window` Cash Registers
- `action_bank_statement_tree_bank`: `view`
- `action_credit_statement_tree`: `act_window` Credit Statements
- `action_bank_statement_tree`: `act_window` Bank Statements

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
