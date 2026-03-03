<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_journal_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/account_journal_views.xml`
- Views: 6
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_account_journal_group_form`
- Name: account.journal.group.form
- Model: `account.journal.group`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `company_id`, `excluded_journal_ids`, `name`, `sequence`
- XPath or positional patches: 0

### `view_account_journal_group_tree`
- Name: account.journal.group.list
- Model: `account.journal.group`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `excluded_journal_ids`, `name`, `sequence`
- XPath or positional patches: 0

### `view_account_journal_search`
- Name: account.journal.search
- Model: `account.journal`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `activity_type_id`, `activity_user_id`, `name`
- XPath or positional patches: 0

### `account_journal_view_kanban`
- Name: account.journal.kanban
- Model: `account.journal`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `name`, `type`
- XPath or positional patches: 0

### `view_account_journal_form`
- Name: account.journal.form
- Model: `account.journal`
- Type: inferred from arch
- Root tag: `form`
- Field references: 37
- Sample fields: `active`, `alias_domain_id`, `alias_name`, `available_payment_method_ids`, `bank_account_id`, `bank_id`, `bank_statements_source`, `code`, `company_id`, `company_partner_id`, and 27 more
- Buttons: `%(action_account_moves_all_a)d`
- XPath or positional patches: 0

### `view_account_journal_tree`
- Name: account.journal.list
- Model: `account.journal`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `active`, `code`, `company_id`, `currency_id`, `default_account_id`, `journal_group_ids`, `name`, `sequence`, `type`
- XPath or positional patches: 0

## Actions

- `action_account_journal_group_list`: `act_window` Multi-ledger
- `action_account_journal_form`: `act_window` Journals

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
