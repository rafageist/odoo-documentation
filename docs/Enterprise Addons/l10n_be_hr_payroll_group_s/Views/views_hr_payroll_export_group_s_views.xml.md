---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payroll_export_group_s_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_group_s/l10n_be_hr_payroll_group_s|l10n_be_hr_payroll_group_s]]
- Scope: Enterprise Addons
- Source file: `views/hr_payroll_export_group_s_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_export_group_s_employee_list_view`
- Name: l10n.be.hr.payroll.export.group.s.employee.list
- Model: `l10n.be.hr.payroll.export.group.s.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_employee_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_group_s_list_view`
- Name: hr.payroll.export.group.s.list
- Model: `l10n.be.hr.payroll.export.group.s`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_group_s_form_view`
- Name: hr.payroll.export.group.s.form
- Model: `l10n.be.hr.payroll.export.group.s`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_form_view`
- Field references: 0
- XPath or positional patches: 0

## Actions

- `l10n_be_export_group_s_action`: `act_window` Export to Group S

## Menus

- `menu_l10n_be_export_work_entries_group_s`: Export Work Entries to Group S

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_group_s/Views]]

