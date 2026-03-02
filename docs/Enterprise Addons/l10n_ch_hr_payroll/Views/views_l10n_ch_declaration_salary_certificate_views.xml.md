<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_declaration_salary_certificate_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_declaration_salary_certificate_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_l10n_ch_certificate_report_form`
- Name: l10n.ch.salary.certificate.form
- Model: `l10n.ch.salary.certificate`
- Type: inferred from arch
- Inherits: `l10n_ch_hr_payroll.l10n_ch_swissdec_transmitter_form`
- Root tag: `div`
- Field references: 6
- Sample fields: `company_id`, `original_date`, `previous_declaration`, `tax_rectificate_employee_ids`, `tax_rectificate_type`, `wage_statement_count`
- Buttons: `action_open_wage_statements`, `generate_tax_accounting_reports`, `send_tax_accounting_reports`
- XPath or positional patches: 2

## Actions

- `action_l10n_ch_certificate`: `act_window` Tax Salaries Declaration

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
