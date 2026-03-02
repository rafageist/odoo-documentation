<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# reports/budget_report_view.xml

- Module: [[docs/Enterprise Addons/account_budget/account_budget|account_budget]]
- Scope: Enterprise Addons
- Source file: `reports/budget_report_view.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `budget_report_view_pivot`
- Name: budget.report.view.pivot
- Model: `budget.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `account_id`, `achieved`, `budget`, `budget_analytic_id`
- XPath or positional patches: 0

### `budget_report_view_graph`
- Name: budget.report.view.graph
- Model: `budget.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `account_id`, `date`
- XPath or positional patches: 0

### `budget_report_view_search`
- Name: budget.report.view.search
- Model: `budget.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `account_id`, `budget_analytic_id`, `company_id`, `date`, `description`, `user_id`
- XPath or positional patches: 0

### `budget_report_view_tree`
- Name: budget.report.view.list
- Model: `budget.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `account_id`, `achieved`, `budget`, `company_id`, `date`, `description`, `line_type`, `user_id`
- XPath or positional patches: 0

## Actions

- `budget_report_action`: `act_window` Budget Report

## Menus

- `budget_report_menu`: Budget Report

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_budget/Views]]

<!-- GENERATED:VIEWFILE -->
