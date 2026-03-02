<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_run_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/l10n_hk_hr_payroll_empf|l10n_hk_hr_payroll_empf]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_run_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_payslip_run_kanban_inherit_l10n_hk_hr_payroll_empf`
- Name: hr.payslip.run.kanban.inherit.l10n_hk_hr_payroll_empf
- Model: `hr.payslip.run`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_payslip_run_view_kanban`
- Root tag: `button`
- Field references: 1
- Sample fields: `l10n_hk_payroll_empf_report_id`
- Buttons: `action_open_empf_contribution_report`, `action_payment_report`
- XPath or positional patches: 1

### `hr_payslip_run_form_inherit_l10n_hk_hr_payroll_empf`
- Name: hr.payslip.run.form.inherit.l10n_hk_hr_payroll_empf
- Model: `hr.payslip.run`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_payslip_run_form`
- Root tag: `field`
- Field references: 4
- Sample fields: `country_code`, `l10n_hk_payroll_group_id`, `l10n_hk_payroll_scheme_id`, `schedule_pay`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/Views]]

<!-- GENERATED:VIEWFILE -->
