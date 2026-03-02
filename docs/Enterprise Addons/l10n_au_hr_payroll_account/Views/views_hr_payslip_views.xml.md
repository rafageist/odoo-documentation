<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_account/l10n_au_hr_payroll_account|l10n_au_hr_payroll_account]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_hr_payslip_filter`
- Name: hr.payslip.view.search.inherit
- Model: `hr.payslip`
- Type: inferred from arch
- Inherits: `hr_payroll.view_hr_payslip_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_hr_payslip_tree`
- Name: hr.payslip.view.list.inherit
- Model: `hr.payslip`
- Type: inferred from arch
- Inherits: `hr_payroll.view_hr_payslip_tree`
- Root tag: `list`
- Field references: 2
- Sample fields: `l10n_au_finalised`, `l10n_au_stp_status`
- XPath or positional patches: 1

### `view_hr_payslip_form`
- Name: hr.payslip.form.inherit.l10n_au_hr_payroll
- Model: `hr.payslip`
- Type: inferred from arch
- Inherits: `hr_payroll.view_hr_payslip_form`
- Root tag: `button`
- Field references: 4
- Sample fields: `has_superstream`, `l10n_au_stp_count`, `l10n_au_stp_status`, `struct_id`
- Buttons: `action_open_payslip_stp`, `action_open_superstream`, `action_payslip_paid`, `action_payslip_payment_report`, `action_register_payment`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_account/Views]]

<!-- GENERATED:VIEWFILE -->
