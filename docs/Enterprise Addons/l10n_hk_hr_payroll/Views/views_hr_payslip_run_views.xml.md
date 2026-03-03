---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_run_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll/l10n_hk_hr_payroll|l10n_hk_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_run_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_payslip_run_kanban_inherit_l10n_hk_hr_payroll`
- Name: hr.payslip.run.kanban.inherit.l10n_hk_hr_payroll
- Model: `hr.payslip.run`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_payslip_run_view_kanban`
- Root tag: `button`
- Field references: 5
- Sample fields: `l10n_hk_autopay`, `l10n_hk_autopay_export_first_batch_date`, `l10n_hk_autopay_export_first_batch_filename`, `l10n_hk_autopay_export_second_batch_date`, `l10n_hk_autopay_export_second_batch_filename`
- Buttons: `action_open_hsbc_autopay_wizard`, `action_paid`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll/Views]]

