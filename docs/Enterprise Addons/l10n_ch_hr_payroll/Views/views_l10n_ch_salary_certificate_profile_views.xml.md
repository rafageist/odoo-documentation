---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_salary_certificate_profile_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_salary_certificate_profile_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_l10n_ch_salary_certificate_profile_form`
- Name: l10n.ch.salary.certificate.profile.form
- Model: `l10n.ch.salary.certificate.profile`
- Type: inferred from arch
- Root tag: `form`
- Field references: 36
- Sample fields: `certificate_template_id`, `company_id`, `employee_id`, `l10n_ch_certificate_type`, `l10n_ch_child_allowance_indirect`, `l10n_ch_cs_additional_text`, `l10n_ch_cs_car_policy`, `l10n_ch_cs_employee_parti_fair_market_value`, `l10n_ch_cs_employee_parti_fair_market_value_canton`, `l10n_ch_cs_employee_parti_fair_market_value_date`, and 26 more
- Buttons: `action_update_all_certificates`
- XPath or positional patches: 0

### `view_l10n_ch_salary_certificate_profile_tree`
- Name: l10n.ch.salary.certificate.profile.tree
- Model: `l10n.ch.salary.certificate.profile`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `company_id`, `l10n_ch_certificate_type`, `name`
- XPath or positional patches: 0

## Actions

- `action_l10n_ch_salary_certificate_profile`: `act_window` Wage Statement Profile

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

