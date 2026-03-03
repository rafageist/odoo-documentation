---
tags: [odoo, enterprise, generated, views]
---

# views/hr_views.xml

- Module: [[docs/Enterprise Addons/planning/planning|planning]]
- Scope: Enterprise Addons
- Source file: `views/hr_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_view_form_email`
- Name: hr.employee.public.view.form
- Model: `hr.employee.public`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `name`, `user_id`, `work_email`
- XPath or positional patches: 0

### `hr_employee_view_form_simplified`
- Name: hr.employee.public.view.form
- Model: `hr.employee.public`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `coach_id`, `company_id`, `department_id`, `image_1920`, `job_id`, `mobile_phone`, `name`, `parent_id`, `user_id`, `work_email`, and 1 more
- XPath or positional patches: 0

### `hr_employee_public_view_form`
- Name: hr.employee.public.form.inherit.planning
- Model: `hr.employee.public`
- Type: inferred from arch
- Inherits: `hr.hr_employee_public_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `has_slots`
- Buttons: `action_view_planning`
- XPath or positional patches: 1

### `view_employee_filter_inherit_hr`
- Name: hr.employee.view.search.inherit
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `planning_role_ids`
- XPath or positional patches: 2

### `hr_employee_view_form_inherit`
- Name: hr.employee.view.form.planning
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `group`
- Field references: 3
- Sample fields: `default_planning_role_id`, `has_slots`, `planning_role_ids`
- Buttons: `action_open_versions`, `action_view_planning`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/planning/Views]]

