<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_account_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/account_account_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_account_search`
- Name: account.account.search
- Model: `account.account`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `account_type`, `name`, `root_id`
- XPath or positional patches: 0

### `view_account_account_kanban`
- Name: account.account.kanban
- Model: `account.account`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `account_type`, `code`, `name`
- XPath or positional patches: 0

### `view_account_list`
- Name: account.account.list
- Model: `account.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `account_type`, `active`, `code`, `company_ids`, `currency_id`, `group_id`, `internal_group`, `name`, `non_trade`, `placeholder_code`, and 3 more
- XPath or positional patches: 0

### `view_account_form`
- Name: account.account.form
- Model: `account.account`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `account_type`, `active`, `code`, `code_mapping_ids`, `company_id`, `company_ids`, `currency_id`, `current_balance`, `description`, `group_id`, and 6 more
- Buttons: `account.action_move_line_select`, `action_open_related_taxes`
- XPath or positional patches: 0

## Actions

- `action_unmerge_accounts`: `server` Unmerge account
- `action_account_form`: `act_window` Chart of Accounts

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
