<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_analytic_line_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/account_analytic_line_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_account_analytic_line_pivot`
- Name: account.analytic.line.pivot
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `analytic.view_account_analytic_line_pivot`
- Root tag: `field`
- Field references: 2
- Sample fields: `account_id`, `partner_id`
- XPath or positional patches: 0

### `view_account_analytic_line_filter_inherit_account`
- Name: account.analytic.line.select.inherit.account
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `analytic.view_account_analytic_line_filter`
- Root tag: `data`
- Field references: 5
- Sample fields: `account_id`, `auto_account_id`, `general_account_id`, `partner_id`, `product_id`
- XPath or positional patches: 3

### `view_account_analytic_line_tree_inherit_account`
- Name: account.analytic.line.list.inherit.account
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `analytic.view_account_analytic_line_tree`
- Root tag: `data`
- Field references: 4
- Sample fields: `general_account_id`, `move_line_id`, `product_id`, `ref`
- XPath or positional patches: 1

### `view_account_analytic_line_form_inherit_account`
- Name: account.analytic.line.form.inherit.account
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `analytic.view_account_analytic_line_form`
- Root tag: `data`
- Field references: 5
- Sample fields: `general_account_id`, `move_line_id`, `partner_id`, `product_id`, `ref`
- XPath or positional patches: 3

## Actions

- `action_analytic_reporting`: `act_window` Analytic Reporting
- `analytic.account_analytic_line_action_entries`: `act_window`

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
