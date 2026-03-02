<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_analytic_account_views.xml

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `views/account_analytic_account_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_move_form_inherit_sale_subscription`
- Name: account.move.form.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `subscription_id`
- XPath or positional patches: 1

### `view_move_line_form_inherit_sale_subscription`
- Name: account.move.line.form.inherit
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `subscription_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Views]]

<!-- GENERATED:VIEWFILE -->
