---
tags: [odoo, enterprise, generated, views]
---

# views/account_fiscal_year_view.xml

- Module: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]]
- Scope: Enterprise Addons
- Source file: `views/account_fiscal_year_view.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `action_account_fiscal_year_tree`
- Name: account.fiscal.year.list
- Model: `account.fiscal.year`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `date_from`, `date_to`, `name`
- XPath or positional patches: 0

### `action_account_fiscal_year_search`
- Name: account.fiscal.year.search
- Model: `account.fiscal.year`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `action_account_fiscal_year_form`
- Name: account.fiscal.year.form
- Model: `account.fiscal.year`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `company_id`, `date_from`, `date_to`, `name`
- XPath or positional patches: 0

## Actions

- `actions_account_fiscal_year`: `act_window` Fiscal Years

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_accountant/Views]]

