<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_deferred_entries_tree`
- Name: account.move.line.deferral.entries.list
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 11

### `view_bank_rec_edit_line`
- Name: account.move.line.bank.rec.edit.line
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `account_id`, `amount_currency`, `analytic_distribution`, `balance`, `company_currency_id`, `currency_id`, `date`, `full_amount_switch_html`, `has_invalid_analytics`, `move_id`, and 3 more
- XPath or positional patches: 0

### `view_move_form_inherit`
- Name: account.move.form.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `deferred_end_date`, `deferred_entry_type`, `deferred_move_ids`, `deferred_original_move_ids`, `deferred_start_date`, `inalterable_hash`
- Buttons: `action_open_bank_reconciliation_widget`, `action_open_bank_reconciliation_widget_statement`, `open_deferred_entries`, `open_deferred_original_entry`
- XPath or positional patches: 5

### `view_move_line_payment_tree`
- Name: account.move.line.payment.list
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_payment_tree`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_reconcile`
- XPath or positional patches: 1

### `view_move_line_tree`
- Name: account.move.line.list
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `deferred_end_date`, `deferred_start_date`, `has_deferred_moves`, `is_account_reconcile`
- Buttons: `action_reconcile`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_accountant/Views]]

<!-- GENERATED:VIEWFILE -->
