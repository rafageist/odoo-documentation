<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# wizard/hr_salary_register.xml

- Module: [[docs/Enterprise Addons/l10n_in_hr_payroll/l10n_in_hr_payroll|l10n_in_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `wizard/hr_salary_register.xml`
- Views: 2
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `hr_employee_tree_inherit`
- Name: hr.employee.list.inherit
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `activity_date_deadline`, `activity_ids`, `company_id`, `parent_id`
- XPath or positional patches: 0

### `view_salary_register`
- Name: Salary Register
- Model: `salary.register.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `date_from`, `date_to`, `department_id`, `employee_ids`, `include_done`, `include_paid`, `job_id`, `name`, `registration_number`, `struct_id`
- Buttons: `action_export_xlsx`
- XPath or positional patches: 0

## Actions

- `action_salary_register`: `act_window` Salary Register

## Menus

- `menu_salary_register`: Salary Register
- `menu_reporting_l10n_in`: India

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_in_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
