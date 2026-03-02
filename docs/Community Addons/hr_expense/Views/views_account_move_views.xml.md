<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/hr_expense/hr_expense|hr_expense]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_move_list_expense`
- Name: account.move.hr.expense.list
- Model: `account.move`
- Type: inferred from arch
- Root tag: `list`
- Field references: 18
- Sample fields: `activity_ids`, `amount_residual_signed`, `amount_tax_signed`, `amount_total_in_currency_signed`, `amount_untaxed_in_currency_signed`, `checked`, `company_currency_id`, `company_id`, `currency_id`, `date`, and 8 more
- XPath or positional patches: 0

### `view_move_form_inherit_expense`
- Name: account.move.form.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `nb_expenses`
- Buttons: `action_open_expense`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/hr_expense/Views]]

<!-- GENERATED:VIEWFILE -->
