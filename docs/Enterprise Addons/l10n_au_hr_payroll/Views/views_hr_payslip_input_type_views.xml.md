---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_input_type_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll/l10n_au_hr_payroll|l10n_au_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_input_type_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `he_payslip_input_type_view_search`
- Name: hr.payslip.input.type.search.inherit
- Model: `hr.payslip.input.type`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_payslip_input_type_view_search`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `l10n_au_payment_type`, `name`
- XPath or positional patches: 1

### `hr_payslip_input_type_view_form`
- Name: hr.payslip.input.type.form.inherit.l10n_au_hr_payroll
- Model: `hr.payslip.input.type`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_payslip_input_type_view_form`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `country_code`, `currency_id`, `l10n_au_default_amount`, `l10n_au_etp_type`, `l10n_au_paygw_treatment`, `l10n_au_payment_type`, `l10n_au_payroll_code`, `l10n_au_payroll_code_description`, `l10n_au_superannuation_treatment`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll/Views]]

