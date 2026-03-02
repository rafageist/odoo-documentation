<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/analytic_line_views.xml

- Module: [[docs/Community Addons/analytic/analytic|analytic]]
- Scope: Community Addons
- Source file: `views/analytic_line_views.xml`
- Views: 6
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_account_analytic_line_kanban`
- Name: account.analytic.line.kanban
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `account_id`, `amount`, `currency_id`, `date`, `name`
- XPath or positional patches: 0

### `view_account_analytic_line_pivot`
- Name: account.analytic.line.pivot
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `account_id`, `amount`, `date`
- XPath or positional patches: 0

### `view_account_analytic_line_graph`
- Name: account.analytic.line.graph
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `account_id`, `amount`, `unit_amount`
- XPath or positional patches: 0

### `view_account_analytic_line_form`
- Name: account.analytic.line.form
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `account_id`, `amount`, `company_id`, `currency_id`, `date`, `name`, `product_uom_id`, `unit_amount`
- XPath or positional patches: 0

### `view_account_analytic_line_filter`
- Name: account.analytic.line.select
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `date`, `name`
- XPath or positional patches: 0

### `view_account_analytic_line_tree`
- Name: account.analytic.line.list
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `account_id`, `amount`, `analytic_distribution`, `company_id`, `currency_id`, `date`, `name`, `partner_id`, `product_uom_id`, `unit_amount`
- XPath or positional patches: 0

## Actions

- `account_analytic_line_action_entries`: `act_window` Analytic Items
- `account_analytic_line_action`: `act_window` Gross Margin

## Navigation

- **Parent:** [[docs/Community Addons/analytic/Views]]

<!-- GENERATED:VIEWFILE -->
