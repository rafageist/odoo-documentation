<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/budget_analytic_views.xml

- Module: [[docs/Enterprise Addons/account_budget/account_budget|account_budget]]
- Scope: Enterprise Addons
- Source file: `views/budget_analytic_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_budget_analytic_search`
- Name: budget.analytic.search
- Model: `budget.analytic`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `date_from`, `date_to`, `name`
- XPath or positional patches: 0

### `view_budget_analytic_kanban`
- Name: budget.analytic.kanban
- Model: `budget.analytic`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `date_from`, `date_to`, `name`, `state`, `user_id`
- XPath or positional patches: 0

### `view_budget_analytic_tree`
- Name: budget.analytic.view.list
- Model: `budget.analytic`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `activity_exception_decoration`, `activity_ids`, `company_id`, `date_from`, `date_to`, `name`, `state`, `user_id`
- Buttons: `%(account_budget.budget_split_wizard_action)d`, `action_open_budget_lines`
- XPath or positional patches: 0

### `view_budget_analytic_form`
- Name: budget.analytic.view.form
- Model: `budget.analytic`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `account_id`, `achieved_amount`, `achieved_percentage`, `budget_amount`, `budget_line_ids`, `budget_type`, `company_id`, `currency_id`, `date_from`, `date_to`, and 7 more
- Buttons: `action_budget_cancel`, `action_budget_confirm`, `action_budget_done`, `action_budget_draft`, `action_open_budget_entries`, `action_open_budget_report`, `create_revised_budget`
- XPath or positional patches: 0

## Actions

- `act_budget_analytic_view`: `act_window` Budgets

## Menus

- `menu_act_budget_analytic_view`: Analytic Budget

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_budget/Views]]

<!-- GENERATED:VIEWFILE -->
