---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_au_super_account_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll/l10n_au_hr_payroll|l10n_au_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_au_super_account_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_au_super_account_view_tree`
- Name: l10n_au.super.account.view.list
- Model: `l10n_au.super.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `employee_id`, `fund_id`, `trustee`, `trustee_name_id`
- XPath or positional patches: 0

### `l10n_au_super_account_view_form`
- Name: l10n_au.super.account.view.form
- Model: `l10n_au.super.account`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `account_active`, `date_from`, `display_name`, `employee_id`, `employee_tfn`, `fund_abn`, `fund_id`, `fund_type`, `member_nbr`, `proportion`, and 3 more
- XPath or positional patches: 0

## Actions

- `l10n_au_super_account_action`: `act_window` Super Accounts

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll/Views]]

