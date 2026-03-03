---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payroll_export_sdworx_view.xml

- Module: [[docs/Enterprise Addons/l10n_it_hr_payroll_sd_worx/l10n_it_hr_payroll_sd_worx|l10n_it_hr_payroll_sd_worx]]
- Scope: Enterprise Addons
- Source file: `views/hr_payroll_export_sdworx_view.xml`
- Views: 3
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `l10n_be_export_sdworx_employee_view_list`
- Name: l10n.it.hr.payroll.export.sdworx.employee.list
- Model: `l10n.it.hr.payroll.export.sdworx.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_employee_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_sdworx_view_list`
- Name: hr.payroll.export.sdworx.list
- Model: `l10n.it.hr.payroll.export.sdworx`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_list_view`
- Field references: 0
- XPath or positional patches: 0

### `hr_payroll_export_sdworx_view_form`
- Name: hr.payroll.export.sdworx.form
- Model: `l10n.it.hr.payroll.export.sdworx`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_work_entry_export_mixin_form_view`
- Field references: 0
- XPath or positional patches: 0

## Actions

- `l10n_it_export_sdworx_action`: `act_window` Export Work Entries to SDWorx

## Menus

- `menu_l10n_it_export_sdworx_leaves_wizard`: Export Work Entries to SDWorx
- `menu_reporting_l10n_it`: Italy

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_it_hr_payroll_sd_worx/Views]]

