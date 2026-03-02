<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payroll_structure_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payroll_structure_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_hr_employee_grade_form`
- Name: hr.payroll.structure.form
- Model: `hr.payroll.structure`
- Type: inferred from arch
- Root tag: `form`
- Field references: 18
- Sample fields: `active`, `category_id`, `code`, `country_id`, `hide_basic_on_pdf`, `id`, `input_line_type_ids`, `name`, `partner_id`, `payslip_name`, and 8 more
- XPath or positional patches: 0

### `view_hr_payroll_structure_filter`
- Name: hr.payroll.structure.select
- Model: `hr.payroll.structure`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `type_id`
- XPath or positional patches: 0

### `view_hr_payroll_structure_list_view`
- Name: hr.payroll.structure.list
- Model: `hr.payroll.structure`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `country_id`, `name`, `rule_ids`, `type_id`
- XPath or positional patches: 0

## Actions

- `action_view_hr_payroll_structure_from_type`: `act_window` Salary Structures
- `action_view_hr_payroll_structure_list_form`: `act_window` Salary Structures

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
