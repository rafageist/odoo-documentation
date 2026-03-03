<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_cash_rounding_view.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/account_cash_rounding_view.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `rounding_tree_view`
- Name: account.cash.rounding.list
- Model: `account.cash.rounding`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `name`, `rounding`, `rounding_method`
- XPath or positional patches: 0

### `rounding_search_view`
- Name: account.cash.rounding.search
- Model: `account.cash.rounding`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `rounding_form_view`
- Name: account.cash.rounding.form
- Model: `account.cash.rounding`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `loss_account_id`, `name`, `profit_account_id`, `rounding`, `rounding_method`, `strategy`
- XPath or positional patches: 0

## Actions

- `rounding_list_action`: `act_window` Cash Roundings

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
