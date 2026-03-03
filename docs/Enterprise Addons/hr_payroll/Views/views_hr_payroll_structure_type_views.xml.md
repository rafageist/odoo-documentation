---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payroll_structure_type_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payroll_structure_type_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_payroll_structure_type_view_search`
- Name: hr.payroll.structure.type.search
- Model: `hr.payroll.structure.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `hr_payroll_structure_type_view_tree`
- Name: hr.payroll.structure.type.list
- Model: `hr.payroll.structure.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `country_code`, `country_id`, `default_resource_calendar_id`, `default_schedule_pay`, `default_struct_id`, `name`, `sequence`, `struct_ids`, `wage_type`
- XPath or positional patches: 0

### `hr_payroll_structure_type_view_form`
- Name: hr.payroll.structure.type.form
- Model: `hr.payroll.structure.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `country_code`, `country_id`, `default_resource_calendar_id`, `default_schedule_pay`, `default_struct_id`, `default_work_entry_type_id`, `name`, `struct_ids`, `struct_type_count`, `wage_type`
- Buttons: `%(action_view_hr_payroll_structure_from_type)d`
- XPath or positional patches: 0

## Actions

- `action_hr_payroll_structure_type`: `act_window` Structure Types

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

