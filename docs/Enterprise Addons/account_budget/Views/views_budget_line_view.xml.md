---
tags: [odoo, enterprise, generated, views]
---

# views/budget_line_view.xml

- Module: [[docs/Enterprise Addons/account_budget/account_budget|account_budget]]
- Scope: Enterprise Addons
- Source file: `views/budget_line_view.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_budget_line_graph`
- Name: budget.line.graph
- Model: `budget.line`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `achieved_amount`, `budget_amount`, `budget_analytic_id`
- XPath or positional patches: 0

### `view_budget_line_pivot`
- Name: budget.line.pivot
- Model: `budget.line`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `achieved_amount`, `budget_amount`, `budget_analytic_id`
- XPath or positional patches: 0

### `view_budget_line_form`
- Name: budget.line.form
- Model: `budget.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `account_id`, `achieved_amount`, `budget_amount`, `budget_analytic_id`, `budget_analytic_state`, `company_id`, `date_from`, `date_to`, `theoritical_amount`
- XPath or positional patches: 0

### `view_budget_line_tree`
- Name: budget.line.list
- Model: `budget.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `account_id`, `achieved_amount`, `budget_amount`, `budget_analytic_id`, `budget_analytic_state`, `company_id`, `currency_id`, `date_from`, `date_to`
- XPath or positional patches: 0

### `view_budget_line_search`
- Name: account.budget.line.search
- Model: `budget.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `account_id`, `budget_analytic_id`
- XPath or positional patches: 0

## Actions

- `act_budget_lines_view`: `act_window` Budgets Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_budget/Views]]

