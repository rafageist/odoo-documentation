---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll/l10n_au_hr_payroll|l10n_au_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_hr_payslip_tree`
- Name: hr.payslip.view.list.inherit
- Model: `hr.payslip`
- Type: inferred from arch
- Inherits: `hr_payroll.view_hr_payslip_tree`
- Root tag: `list`
- Field references: 1
- Sample fields: `l10n_au_schedule_pay`
- XPath or positional patches: 1

### `view_hr_payslip_form`
- Name: hr.payslip.form.inherit.l10n_au_hr_payroll
- Model: `hr.payslip`
- Type: inferred from arch
- Inherits: `hr_payroll.view_hr_payslip_form`
- Root tag: `xpath`
- Field references: 16
- Sample fields: `city_id`, `country_id`, `date`, `input_line_ids`, `input_uom`, `l10n_au_exempt_foreign_income`, `l10n_au_foreign_tax_withheld`, `l10n_au_income_stream_type`, `l10n_au_other_input_details_ids`, `l10n_au_termination_type`, and 6 more
- XPath or positional patches: 3

### `view_hr_payslip_filter`
- Name: hr.payslip.view.search.inherit
- Model: `hr.payslip`
- Type: inferred from arch
- Inherits: `hr_payroll.view_hr_payslip_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll/Views]]

