---
tags: [odoo, enterprise, generated, views]
---

# views/account_reconcile_views.xml

- Module: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]]
- Scope: Enterprise Addons
- Source file: `views/account_reconcile_views.xml`
- Views: 3
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `account_accountant_view_account_reconcile_model_search`
- Name: account.reconcile.model.search
- Model: `account.reconcile.model`
- Type: inferred from arch
- Inherits: `account.view_account_reconcile_model_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_move_line_reconcile_tree`
- Name: account.move.line.list.reconcile
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 34
- Sample fields: `account_id`, `account_type`, `amount_currency`, `amount_residual`, `amount_residual_currency`, `analytic_distribution`, `balance`, `company_currency_id`, `company_id`, `credit`, and 24 more
- Buttons: `action_reconcile`
- XPath or positional patches: 0

### `view_account_move_line_reconcile_search`
- Name: account.move.line.reconcile.search
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 13
- Sample fields: `account_id`, `account_type`, `balance`, `date`, `invoice_date`, `journal_id`, `move_id`, `name`, `partner_id`, `reconcile_model_id`, and 3 more
- XPath or positional patches: 0

## Actions

- `account.action_account_reconcile_model`: `act_window`
- `action_move_line_posted_unreconciled`: `act_window` Journal Items to reconcile
- `action_open_auto_reconcile_wizard`: `act_window` Reconcile automatically

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_accountant/Views]]

