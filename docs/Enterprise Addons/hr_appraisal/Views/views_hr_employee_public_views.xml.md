---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_public_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_public_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_public_select_from_goal_view_list`
- Name: hr.employee.public.select.from.goal.view.list
- Model: `hr.employee.public`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `department_id`, `employee_id`, `job_id`
- XPath or positional patches: 0

### `hr_employee_public_view_form`
- Name: hr.employee.public.view.form.inherit.appraisal
- Model: `hr.employee.public`
- Type: inferred from arch
- Inherits: `hr.hr_employee_public_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `last_appraisal_date`
- Buttons: `action_open_last_appraisal`, `action_send_appraisal_request`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal/Views]]

