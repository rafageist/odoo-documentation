<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_salary_attachment_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_salary_attachment_views.xml`
- Views: 6
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `hr_salary_attachment_view_search`
- Name: hr.salary.attachment.search
- Model: `hr.salary.attachment`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `description`, `employee_ids`, `other_input_type_id`, `state`
- XPath or positional patches: 0

### `hr_salary_attachment_employee_view_form`
- Name: hr.salary.attachment.form
- Model: `hr.salary.attachment`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_salary_attachment_view_form`
- Root tag: `header`
- Field references: 1
- Sample fields: `state`
- Buttons: `action_close`, `action_open`, `action_split`, `action_unlink`
- XPath or positional patches: 3

### `hr_salary_attachment_view_form`
- Name: hr.salary.attachment.form
- Model: `hr.salary.attachment`
- Type: inferred from arch
- Root tag: `form`
- Field references: 22
- Sample fields: `attachment_name`, `company_id`, `currency_id`, `date_end`, `date_estimated_end`, `date_start`, `description`, `duration_type`, `employee_count`, `employee_ids`, and 12 more
- Buttons: `action_close`, `action_open`, `action_open_payslips`, `action_split`
- XPath or positional patches: 0

### `hr_salary_attachment_view_pivot`
- Name: hr.salary.attachment.pivot
- Model: `hr.salary.attachment`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 6
- Sample fields: `employee_ids`, `monthly_amount`, `other_input_type_id`, `paid_amount`, `remaining_amount`, `total_amount`
- XPath or positional patches: 0

### `hr_salary_attachment_employee_view_list`
- Name: hr.salary.attachment.list
- Model: `hr.salary.attachment`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_salary_attachment_view_tree`
- Root tag: `list`
- Field references: 3
- Sample fields: `date_start`, `employee_ids`, `other_input_type_id`
- Buttons: `action_close`, `action_open`, `action_open_employee_salary_attachment`, `action_split`
- XPath or positional patches: 2

### `hr_salary_attachment_view_tree`
- Name: hr.salary.attachment.list
- Model: `hr.salary.attachment`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `date_end`, `date_start`, `description`, `employee_ids`, `monthly_amount_display`, `other_input_type_id`, `paid_amount`, `remaining_amount`, `state`, `total_amount_display`
- XPath or positional patches: 0

## Actions

- `hr_salary_attachment_action_view_employee`: `act_window` Salary Adjustment
- `hr_salary_attachment_action`: `act_window` Salary Adjustment
- `action_hr_salary_attachment_new`: `act_window` Salary Adjustment

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
