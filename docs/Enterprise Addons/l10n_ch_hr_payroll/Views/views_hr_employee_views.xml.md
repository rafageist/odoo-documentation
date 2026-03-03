---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_view_form`
- Name: hr.employee.view.form.inherit.l10n.ch.hr.payroll
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.payroll_hr_employee_view_form`
- Root tag: `group`
- Field references: 127
- Sample fields: `amount`, `birthdate`, `birthday`, `certificate`, `children`, `contract_date_end`, `contract_date_start`, `contract_type_id`, `country_id`, `description`, and 117 more
- Buttons: `%(hr.hr_version_wizard_action)d`, `action_view_wages`
- XPath or positional patches: 14

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

