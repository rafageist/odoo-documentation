<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_au_employer_registration_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_api/l10n_au_hr_payroll_api|l10n_au_hr_payroll_api]]
- Scope: Enterprise Addons
- Source file: `views/l10n_au_employer_registration_views.xml`
- Views: 2
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `l10n_au_employer_registration_view_form`
- Name: l10n_au.employer.registration.view.form
- Model: `l10n_au.employer.registration`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `company_id`, `create_date`, `odoo_disclaimer_check`, `registration_mode`, `status`, `superchoice_dda_check`
- XPath or positional patches: 0

### `l10n_au_employer_registration_view_tree`
- Name: l10n_au.employer.registration.view.tree
- Model: `l10n_au.employer.registration`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `create_date`, `registration_mode`, `status`
- XPath or positional patches: 0

## Actions

- `l10n_au_employer_registration_action`: `act_window` Employer Registration

## Menus

- `menu_l10n_au_payroll_technical`: Payroll
- `menu_l10n_au_employer_registration`: Employer Registrations

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_api/Views]]

<!-- GENERATED:VIEWFILE -->
