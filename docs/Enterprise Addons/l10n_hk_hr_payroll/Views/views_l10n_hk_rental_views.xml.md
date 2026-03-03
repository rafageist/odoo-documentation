---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_hk_rental_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll/l10n_hk_hr_payroll|l10n_hk_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_hk_rental_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_hk_rental_view_tree`
- Name: l10n_hk.rental.list
- Model: `l10n_hk.rental`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `amount`, `currency_id`, `date_end`, `date_start`, `employee_id`, `name`, `nature`, `state`
- XPath or positional patches: 0

### `l10n_hk_rental_view_form`
- Name: l10n_hk.rental.form
- Model: `l10n_hk.rental`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `active`, `address`, `amount`, `company_id`, `currency_id`, `date_end`, `date_start`, `employee_id`, `name`, `nature`, and 2 more
- Buttons: `action_open_rentals_list`
- XPath or positional patches: 0

## Actions

- `action_l10n_hk_rental`: `act_window` Rentals

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll/Views]]

