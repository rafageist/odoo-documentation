---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payroll_export_partena_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_partena/l10n_be_hr_payroll_partena|l10n_be_hr_payroll_partena]]
- Scope: Enterprise Addons
- Source file: `views/hr_payroll_export_partena_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_export_partena_employee_list_view`
- Name: l10n.be.hr.payroll.export.partena.employee.list
- Model: `l10n.be.hr.payroll.export.partena.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_employee_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_partena_list_view`
- Name: hr.payroll.export.partena.list
- Model: `l10n.be.hr.payroll.export.partena`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_partena_form_view`
- Name: hr.payroll.export.partena.form
- Model: `l10n.be.hr.payroll.export.partena`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_form_view`
- Field references: 0
- XPath or positional patches: 0

## Actions

- `l10n_be_export_partena_action`: `act_window` Export to Partena

## Menus

- `menu_l10n_be_export_work_entries_partena`: Export Work Entries to Partena

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_partena/Views]]

