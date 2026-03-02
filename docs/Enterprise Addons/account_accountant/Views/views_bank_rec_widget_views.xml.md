<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/bank_rec_widget_views.xml

- Module: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]]
- Scope: Enterprise Addons
- Source file: `views/bank_rec_widget_views.xml`
- Views: 13
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `view_bank_statement_tree`
- Name: account.bank.statement.list
- Model: `account.bank.statement`
- Type: inferred from arch
- Inherits: `account.view_bank_statement_tree`
- Root tag: `list`
- Field references: 0
- Buttons: `action_open_bank_reconcile_widget`
- XPath or positional patches: 1

### `view_account_search_bank_rec_widget`
- Name: account.account.search.bank.rec.widget
- Model: `account.account`
- Type: inferred from arch
- Inherits: `account.view_account_search`
- Root tag: `field`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_account_list_bank_rec_widget`
- Name: account.account.list.bank.rec.widget
- Model: `account.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `account_type`, `code`, `description`, `group_id`, `name`, `reconcile`
- XPath or positional patches: 0

### `view_account_move_line_list_bank_rec_widget`
- Name: account.move.line.list.bank_rec_widget
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 15
- Sample fields: `account_id`, `amount_residual`, `amount_residual_currency`, `analytic_distribution`, `company_currency_id`, `currency_id`, `date`, `date_maturity`, `invoice_date`, `journal_id`, and 5 more
- XPath or positional patches: 0

### `view_move_form_bank_rec_widget`
- Name: account.move.form.bank_rec_widget
- Model: `account.move`
- Type: inferred from arch
- Root tag: `form`
- Field references: 0
- XPath or positional patches: 0

### `view_bank_statement_line_quick_create_form_bank_rec_widget`
- Name: account.bank.statement.line.form.bank_rec_widget
- Model: `account.bank.statement.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `amount`, `currency_id`, `date`, `journal_id`, `partner_id`, `payment_ref`
- XPath or positional patches: 0

### `view_bank_statement_line_form_bank_rec_widget`
- Name: account.bank.statement.line.form.bank_rec_widget
- Model: `account.bank.statement.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `amount`, `amount_currency`, `company_id`, `currency_id`, `date`, `foreign_currency_id`, `is_reconciled`, `journal_id`, `partner_id`, `payment_ref`, and 4 more
- Buttons: `action_button_draft`, `action_save_close`, `action_save_new`
- XPath or positional patches: 0

### `view_bank_statement_line_tree_bank_rec_widget`
- Name: account.bank.statement.line.list.bank_rec_widget
- Model: `account.bank.statement.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 23
- Sample fields: `account_number`, `amount`, `amount_currency`, `checked`, `company_id`, `country_code`, `currency_id`, `date`, `foreign_currency_id`, `is_reconciled`, and 13 more
- XPath or positional patches: 0

### `view_bank_statement_line_kanban_bank_rec_widget`
- Name: account.bank.statement.line.kanban.bank_rec_widget
- Model: `account.bank.statement.line`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 25
- Sample fields: `account_number`, `activity_ids`, `amount`, `amount_currency`, `bank_statement_attachment_ids`, `checked`, `company_id`, `currency_id`, `date`, `foreign_currency_id`, and 15 more
- XPath or positional patches: 0

### `view_bank_statement_line_search_bank_rec_widget`
- Name: account.bank.statement.line.search.bank_rec_widget
- Model: `account.bank.statement.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 14
- Sample fields: `activity_ids`, `amount`, `date`, `id`, `is_reconciled`, `journal_id`, `move_id`, `name`, `narration`, `partner_id`, and 4 more
- XPath or positional patches: 0

### `view_account_move_line_search_bank_rec_widget`
- Name: account.move.line.search.bank_rec_widget
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 8
- Sample fields: `account_id`, `currency_id`, `date`, `invoice_date`, `journal_id`, `move_id`, `name`, `partner_id`
- XPath or positional patches: 0

### `view_bank_create_statement_form_bank_rec_widget`
- Name: account.create.bank.statement.form.bank_rec_widget
- Model: `account.bank.statement`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `attachment_ids`, `balance_end`, `balance_end_real`, `balance_start`, `line_ids`, `name`
- Buttons: `action_open_bank_reconcile_widget`
- XPath or positional patches: 0

### `view_bank_statement_form_bank_rec_widget`
- Name: account.bank.statement.form.bank_rec_widget
- Model: `account.bank.statement`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `account_number`, `amount`, `amount_currency`, `balance_end`, `balance_end_real`, `balance_start`, `create_date`, `currency_id`, `date`, `foreign_currency_id`, and 6 more
- Buttons: `action_open_bank_reconcile_widget`
- XPath or positional patches: 0

## Actions

- `model_account_statement_line_button_draft`: `server` Reset to draft
- `action_bank_statement_attachment`: `server` Statement
- `action_bank_statement_line_transactions_kanban`: `act_window` Bank Matching
- `action_bank_statement_line_transactions`: `act_window` Bank Matching
- `action_bank_statement_line_form_bank_rec_widget`: `act_window` New Transaction
- `action_bank_statement_form_bank_rec_widget`: `act_window` Create Statement

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_accountant/Views]]

<!-- GENERATED:VIEWFILE -->
