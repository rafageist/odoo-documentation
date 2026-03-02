<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_loan_views.xml

- Module: [[docs/Enterprise Addons/account_loans/account_loans|account_loans]]
- Scope: Enterprise Addons
- Source file: `views/account_loan_views.xml`
- Views: 10
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `account_loan_view_account_move_list_view`
- Name: account.move.list
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `account_loan_line_pivot_view`
- Name: account.loan.line.pivot
- Model: `account.loan.line`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `date`, `interest`, `loan_id`, `payment`, `principal`
- XPath or positional patches: 0

### `account_loan_line_search_view`
- Name: account.loan.line.search
- Model: `account.loan.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `loan_name`
- XPath or positional patches: 0

### `account_loan_line_list_view`
- Name: account.loan.line.list
- Model: `account.loan.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `currency_id`, `date`, `interest`, `long_term_theoretical_balance`, `outstanding_balance`, `payment`, `principal`, `sequence`, `short_term_theoretical_balance`
- XPath or positional patches: 0

### `account_loan_graph_view`
- Name: account.loan.graph
- Model: `account.loan`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `amount_borrowed`, `date`, `interest`, `name`
- XPath or positional patches: 0

### `account_loan_pivot_view`
- Name: account.loan.pivot
- Model: `account.loan`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `amount_borrowed`, `date`, `name`
- XPath or positional patches: 0

### `account_loan_kanban_view`
- Name: account.loan.search
- Model: `account.loan`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `amount_borrowed`, `currency_id`, `date`, `name`, `state`
- XPath or positional patches: 0

### `account_loan_search_view`
- Name: account.loan.search
- Model: `account.loan`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `asset_group_id`, `loan_properties`, `name`
- XPath or positional patches: 0

### `account_loan_list_view`
- Name: account.loan.list
- Model: `account.loan`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `amount_borrowed`, `currency_id`, `date`, `end_date`, `expense_account_id`, `long_term_account_id`, `name`, `outstanding_balance`, `short_term_account_id`, `state`
- XPath or positional patches: 0

### `account_loan_form_view`
- Name: account.loan.form
- Model: `account.loan`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `amount_borrowed`, `asset_group_id`, `company_id`, `count_linked_assets`, `currency_id`, `date`, `duration`, `expense_account_id`, `interest`, `journal_id`, and 9 more
- Buttons: `action_cancel`, `action_close`, `action_confirm`, `action_open_linked_assets`, `action_open_loan_entries`, `action_reset`, `action_set_to_draft`
- XPath or positional patches: 0

## Actions

- `action_view_account_loans_analysis`: `act_window` Loans Analysis
- `action_view_account_loans`: `act_window` Loans

## Menus

- `menu_action_loans_analysis`: Loans Analysis
- `menu_action_loans`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_loans/Views]]

<!-- GENERATED:VIEWFILE -->
