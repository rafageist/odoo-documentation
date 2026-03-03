---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payroll_export_sdworx_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_sd_worx/l10n_be_hr_payroll_sd_worx|l10n_be_hr_payroll_sd_worx]]
- Scope: Enterprise Addons
- Source file: `views/hr_payroll_export_sdworx_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_export_sdworx_employee_list_view`
- Name: l10n.be.hr.payroll.export.sdworx.employee.list
- Model: `l10n.be.hr.payroll.export.sdworx.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_employee_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_sdworx_list_view`
- Name: hr.payroll.export.sdworx.list
- Model: `l10n.be.hr.payroll.export.sdworx`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_sdworx_form_view`
- Name: hr.payroll.export.sdworx.form
- Model: `l10n.be.hr.payroll.export.sdworx`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_form_view`
- Field references: 0
- XPath or positional patches: 0

## Actions

- `l10n_be_export_sdworx_action`: `act_window` Export Work Entries to SDWorx

## Menus

- `menu_l10n_be_export_work_entries_sdworx`: Export Work Entries to SDWorx

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_sd_worx/Views]]

