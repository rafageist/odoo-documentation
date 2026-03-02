<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payroll_export_prisma_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_prisma/l10n_be_hr_payroll_prisma|l10n_be_hr_payroll_prisma]]
- Scope: Enterprise Addons
- Source file: `views/hr_payroll_export_prisma_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_export_prisma_employee_list_view`
- Name: l10n.be.hr.payroll.export.prisma.employee.list
- Model: `l10n.be.hr.payroll.export.prisma.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_employee_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_prisma_list_view`
- Name: hr.payroll.export.prisma.list
- Model: `l10n.be.hr.payroll.export.prisma`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_prisma_form_view`
- Name: hr.payroll.export.prisma.form
- Model: `l10n.be.hr.payroll.export.prisma`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_form_view`
- Field references: 0
- XPath or positional patches: 0

## Actions

- `l10n_be_export_prisma_action`: `act_window` Export to Prisma

## Menus

- `menu_l10n_be_export_work_entries_prisma`: Export Work Entries to Prisma

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_prisma/Views]]

<!-- GENERATED:VIEWFILE -->
