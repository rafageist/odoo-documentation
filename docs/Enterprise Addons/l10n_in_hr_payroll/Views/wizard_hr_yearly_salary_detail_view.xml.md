---
tags: [odoo, enterprise, generated, views]
---

# wizard/hr_yearly_salary_detail_view.xml

- Module: [[docs/Enterprise Addons/l10n_in_hr_payroll/l10n_in_hr_payroll|l10n_in_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `wizard/hr_yearly_salary_detail_view.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_yearly_salary_detail`
- Name: Employee Yearly Salary
- Model: `yearly.salary.detail`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `department_id`, `employee_ids`, `job_id`, `name`, `registration_number`, `year`
- Buttons: `print_report`
- XPath or positional patches: 0

## Actions

- `action_yearly_salary_detail`: `act_window` Yearly Salary by Employee

## Menus

- `menu_yearly_salary_detail`: Yearly Salary by Employee

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_in_hr_payroll/Views]]

