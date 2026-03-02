<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/analytic_account_views.xml

- Module: [[docs/Community Addons/analytic/analytic|analytic]]
- Scope: Community Addons
- Source file: `views/analytic_account_views.xml`
- Views: 5
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_account_analytic_account_search`
- Name: account.analytic.account.search
- Model: `account.analytic.account`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `partner_id`
- XPath or positional patches: 0

### `view_account_analytic_account_kanban`
- Name: account.analytic.account.kanban
- Model: `account.analytic.account`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `balance`, `currency_id`, `display_name`
- XPath or positional patches: 0

### `view_account_analytic_account_list_select`
- Name: account.analytic.account.list.select
- Model: `account.analytic.account`
- Type: inferred from arch
- Inherits: `analytic.view_account_analytic_account_list`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `view_account_analytic_account_list`
- Name: account.analytic.account.list
- Model: `account.analytic.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `active`, `balance`, `code`, `company_id`, `credit`, `currency_id`, `debit`, `name`, `partner_id`, `plan_id`
- XPath or positional patches: 0

### `view_account_analytic_account_form`
- Name: analytic.analytic.account.form
- Model: `account.analytic.account`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `active`, `balance`, `code`, `company_id`, `currency_id`, `name`, `partner_id`, `plan_id`
- Buttons: `%(account_analytic_line_action)d`
- XPath or positional patches: 0

## Actions

- `action_account_analytic_account_form`: `act_window` Analytic Accounts
- `action_analytic_account_form`: `act_window` Chart of Analytic Accounts

## Navigation

- **Parent:** [[docs/Community Addons/analytic/Views]]

<!-- GENERATED:VIEWFILE -->
