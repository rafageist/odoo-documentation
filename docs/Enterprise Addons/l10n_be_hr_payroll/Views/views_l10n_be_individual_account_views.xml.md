---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_be_individual_account_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_be_individual_account_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_individual_account_view_tree`
- Name: l10n_be.individual.account.tree
- Model: `l10n_be.individual.account`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_payroll_declaration_mixin_view_list`
- Root tag: `list`
- Field references: 2
- Sample fields: `name`, `year`
- XPath or positional patches: 1

### `l10n_be_individual_account_view_form`
- Name: l10n_be.individual.account.form
- Model: `l10n_be.individual.account`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_payroll_declaration_mixin_view_form`
- Root tag: `form`
- Field references: 2
- Sample fields: `name`, `year`
- XPath or positional patches: 1

## Actions

- `l10n_be_individual_account_action`: `act_window` Individual Accounts

## Menus

- `menu_l10n_be_individual_account`: Individual Accounts

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

