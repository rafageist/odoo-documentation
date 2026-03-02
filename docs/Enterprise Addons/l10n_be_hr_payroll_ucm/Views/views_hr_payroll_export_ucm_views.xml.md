<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payroll_export_ucm_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_ucm/l10n_be_hr_payroll_ucm|l10n_be_hr_payroll_ucm]]
- Scope: Enterprise Addons
- Source file: `views/hr_payroll_export_ucm_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_export_ucm_employee_list_view`
- Name: l10n.be.hr.payroll.export.ucm.employee.list
- Model: `l10n.be.hr.payroll.export.ucm.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_employee_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_ucm_list_view`
- Name: hr.payroll.export.ucm.list
- Model: `l10n.be.hr.payroll.export.ucm`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_ucm_form_view`
- Name: hr.payroll.export.ucm.form
- Model: `l10n.be.hr.payroll.export.ucm`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_form_view`
- Field references: 0
- XPath or positional patches: 0

## Actions

- `l10n_be_export_ucm_action`: `act_window` Export to UCM

## Menus

- `menu_l10n_be_export_work_entries_ucm`: Export Work Entries to UCM

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_ucm/Views]]

<!-- GENERATED:VIEWFILE -->
