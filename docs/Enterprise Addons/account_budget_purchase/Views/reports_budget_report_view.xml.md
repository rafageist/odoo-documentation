<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# reports/budget_report_view.xml

- Module: [[docs/Enterprise Addons/account_budget_purchase/account_budget_purchase|account_budget_purchase]]
- Scope: Enterprise Addons
- Source file: `reports/budget_report_view.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `budget_report_view_pivot`
- Name: budget.report.view.pivot
- Model: `budget.report`
- Type: inferred from arch
- Inherits: `account_budget.budget_report_view_pivot`
- Root tag: `field`
- Field references: 2
- Sample fields: `achieved`, `committed`
- XPath or positional patches: 0

### `budget_report_view_graph`
- Name: budget.report.view.graph
- Model: `budget.report`
- Type: inferred from arch
- Inherits: `account_budget.budget_report_view_graph`
- Root tag: `field`
- Field references: 2
- Sample fields: `account_id`, `committed`
- XPath or positional patches: 0

### `budget_report_view_search`
- Name: budget.report.view.search
- Model: `budget.report`
- Type: inferred from arch
- Inherits: `account_budget.budget_report_view_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `budget_report_view_tree`
- Name: budget.report.view.list
- Model: `budget.report`
- Type: inferred from arch
- Inherits: `account_budget.budget_report_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `achieved`, `committed`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_budget_purchase/Views]]

<!-- GENERATED:VIEWFILE -->
