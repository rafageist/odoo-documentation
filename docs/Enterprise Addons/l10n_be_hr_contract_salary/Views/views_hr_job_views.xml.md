---
tags: [odoo, enterprise, generated, views]
---

# views/hr_job_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_contract_salary/l10n_be_hr_contract_salary|l10n_be_hr_contract_salary]]
- Scope: Enterprise Addons
- Source file: `views/hr_job_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_be_hr_job_payroll_view_tree`
- Name: l10n.be.hr.job.payroll.view.list
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `l10n_be_hr_contract_salary.hr_job_payroll_view_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `l10n_be_contract_ip`, `l10n_be_contract_withholding_taxes_exemption`
- XPath or positional patches: 2

### `hr_job_payroll_view_tree`
- Name: hr.job.payroll.view.list
- Model: `hr.job`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `company_id`, `department_id`, `name`
- XPath or positional patches: 0

### `hr_job_view_form`
- Name: hr.job.view.form
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr.view_hr_job_form`
- Root tag: `page`
- Field references: 8
- Sample fields: `display_l10n_be_scale`, `l10n_be_contract_ip`, `l10n_be_contract_withholding_taxes_exemption`, `l10n_be_custom_representation_fees`, `l10n_be_custom_representation_fees_car_management`, `l10n_be_custom_representation_fees_homeworking`, `l10n_be_custom_representation_fees_internet`, `l10n_be_custom_representation_fees_phone`
- XPath or positional patches: 3

## Actions

- `action_hr_job_payroll_configuration`: `server` Job Configuration

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_contract_salary/Views]]

