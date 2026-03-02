<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_work_entry_export_mixin_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_work_entry_export_mixin_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_work_entry_export_employee_mixin_list_view`
- Name: hr.work.entry.export.employee.list
- Model: `hr.work.entry.export.employee.mixin`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `employee_id`, `export_id`, `version_ids`
- XPath or positional patches: 0

### `hr_work_entry_export_mixin_list_view`
- Name: hr.work.entry.export.mixin.list
- Model: `hr.work.entry.export.mixin`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `create_uid`, `export_file`, `export_filename`, `period_start`, `period_stop`
- XPath or positional patches: 0

### `hr_work_entry_export_mixin_form_view`
- Name: hr.work.entry.export.mixin.form
- Model: `hr.work.entry.export.mixin`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `company_id`, `eligible_employee_count`, `export_file`, `export_filename`, `reference_month`, `reference_year`
- Buttons: `action_export_file`, `action_open_employees`, `action_populate`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
