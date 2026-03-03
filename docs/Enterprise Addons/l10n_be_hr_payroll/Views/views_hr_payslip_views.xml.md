---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_hr_payslip_filter`
- Name: hr.payslip.select.inherit.ecovouchers
- Model: `hr.payslip`
- Type: inferred from arch
- Inherits: `hr_payroll.view_hr_payslip_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `hr_payslip_view_form_inherit_double_pay`
- Name: hr.payslip.view.form.double.pay
- Model: `hr.payslip`
- Type: inferred from arch
- Inherits: `hr_payroll.view_hr_payslip_form`
- Root tag: `field`
- Field references: 6
- Sample fields: `l10n_be_is_december`, `l10n_be_is_double_pay`, `l10n_be_max_seizable_amount`, `l10n_be_max_seizable_warning`, `state`, `struct_id`
- Buttons: `%(l10n_be_december_slip_wizard_action)d`, `%(l10n_be_double_pay_recovery_wizard_action)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

