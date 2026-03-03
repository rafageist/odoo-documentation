---
tags: [odoo, enterprise, generated, views]
---

# wizard/account_change_lock_date.xml

- Module: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]]
- Scope: Enterprise Addons
- Source file: `wizard/account_change_lock_date.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_account_change_lock_date`
- Name: account.change.lock.date.form
- Model: `account.change.lock.date`
- Type: inferred from arch
- Root tag: `form`
- Field references: 27
- Sample fields: `company_id`, `exception_applies_to`, `exception_duration`, `exception_reason`, `fiscalyear_lock_date`, `fiscalyear_lock_date_for_everyone`, `fiscalyear_lock_date_for_me`, `hard_lock_date`, `min_fiscalyear_lock_date_exception_for_everyone_id`, `min_fiscalyear_lock_date_exception_for_me_id`, and 17 more
- Buttons: `change_lock_date`
- XPath or positional patches: 0

## Actions

- `action_view_account_change_lock_date`: `act_window` Lock Journal Entries

## Menus

- `menu_action_change_lock_date`: Lock Dates…

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_accountant/Views]]

