---
tags: [odoo, community, generated, views]
---

# views/account_analytic_account_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `views/account_analytic_account_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_analytic_account_list_inherit`
- Name: account.analytic.account.list.inherit
- Model: `account.analytic.account`
- Type: inferred from arch
- Inherits: `analytic.view_account_analytic_account_list`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_count`
- XPath or positional patches: 2

### `account_analytic_account_view_form_inherit`
- Name: account.analytic.account.form.inherit
- Model: `account.analytic.account`
- Type: inferred from arch
- Inherits: `analytic.view_account_analytic_account_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_count`
- Buttons: `action_view_projects`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

