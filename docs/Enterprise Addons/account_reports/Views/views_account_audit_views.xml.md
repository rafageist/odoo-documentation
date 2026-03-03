---
tags: [odoo, enterprise, generated, views]
---

# views/account_audit_views.xml

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_audit_views.xml`
- Views: 4
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `account_audit_account_balances_search_view`
- Name: account.audit.account.balances.search
- Model: `account.account`
- Type: inferred from arch
- Root tag: `search`
- Field references: 10
- Sample fields: `account_type`, `audit_balance`, `audit_credit`, `audit_debit`, `audit_previous_balance`, `audit_status`, `audit_var_n_1`, `audit_var_percentage`, `code`, `name`
- XPath or positional patches: 0

### `account_audit_account_balances_list_view`
- Name: account.audit.account.balances.list
- Model: `account.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 12
- Sample fields: `audit_balance`, `audit_balance_show_warning`, `audit_credit`, `audit_debit`, `audit_previous_balance`, `audit_previous_balance_show_warning`, `audit_status`, `audit_var_n_1`, `audit_var_percentage`, `code`, and 2 more
- XPath or positional patches: 0

### `account_audit_search_view`
- Name: account.audit.search
- Model: `account.return`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `date_deadline`, `date_from`, `date_submission`, `date_to`, `name`, `state`, `type_id`
- XPath or positional patches: 0

### `account_audit_kanban_view`
- Name: account.audit.kanban
- Model: `account.return`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `activity_ids`, `audit_balances_completed_count`, `audit_balances_count`, `audit_status`, `check_count`, `is_completed`, `name`, `resolved_check_count`, `state`
- XPath or positional patches: 0

## Actions

- `action_view_account_audit_checks`: `act_window` Cycle
- `action_view_account_balances`: `act_window` Balances
- `action_view_account_audit`: `act_window` Audit
- `action_create_account_audit`: `act_window` Start an Audit

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Views]]

