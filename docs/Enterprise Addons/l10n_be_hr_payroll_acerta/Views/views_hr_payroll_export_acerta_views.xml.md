---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payroll_export_acerta_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_acerta/l10n_be_hr_payroll_acerta|l10n_be_hr_payroll_acerta]]
- Scope: Enterprise Addons
- Source file: `views/hr_payroll_export_acerta_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_export_acerta_employee_list_view`
- Name: l10n.be.hr.payroll.export.acerta.employee.list
- Model: `l10n.be.hr.payroll.export.acerta.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_employee_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_acerta_list_view`
- Name: hr.payroll.export.acerta.list
- Model: `l10n.be.hr.payroll.export.acerta`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_acerta_form_view`
- Name: hr.payroll.export.acerta.form
- Model: `l10n.be.hr.payroll.export.acerta`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_form_view`
- Field references: 0
- XPath or positional patches: 0

## Actions

- `l10n_be_export_acerta_action`: `act_window` Export to Acerta

## Menus

- `menu_l10n_be_export_work_entries_acerta`: Export Work Entries to Acerta

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_acerta/Views]]

