---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_input_type_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_input_type_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_payslip_input_type_view_kanban`
- Name: hr.payslip.input.type.kanban.view
- Model: `hr.payslip.input.type`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `code`, `name`
- XPath or positional patches: 0

### `hr_payslip_input_type_view_tree`
- Name: hr.payslip.input.type.view.list
- Model: `hr.payslip.input.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `available_in_attachments`, `code`, `country_id`, `name`, `struct_ids`
- XPath or positional patches: 0

### `hr_payslip_input_type_view_form`
- Name: hr.payslip.input.type.view.form
- Model: `hr.payslip.input.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `available_in_attachments`, `code`, `country_code`, `country_id`, `default_no_end_date`, `is_quantity`, `name`, `struct_ids`
- XPath or positional patches: 0

### `hr_payslip_input_type_view_search`
- Name: hr.payslip.input.type.view.search
- Model: `hr.payslip.input.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `struct_ids`
- XPath or positional patches: 0

## Actions

- `action_view_hr_payslip_input_type`: `act_window` Payslip Other Input Types

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

