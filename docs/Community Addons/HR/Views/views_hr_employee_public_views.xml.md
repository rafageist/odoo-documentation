<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_employee_public_views.xml

- Module: [[docs/Community Addons/hr/hr|hr]]
- Scope: Community Addons
- Source file: `views/hr_employee_public_views.xml`
- Views: 4
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `hr_employee_public_view_kanban`
- Name: hr.employee.kanban
- Model: `hr.employee.public`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 11
- Sample fields: `avatar_128`, `birthday_public_display_string`, `hr_icon_display`, `image_1024`, `image_128`, `job_id`, `name`, `show_hr_icon_display`, `user_id`, `work_email`, and 1 more
- XPath or positional patches: 0

### `hr_employee_public_view_tree`
- Name: hr.employee.list
- Model: `hr.employee.public`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `coach_id`, `company_id`, `department_id`, `job_id`, `name`, `parent_id`, `work_email`, `work_phone`
- XPath or positional patches: 0

### `hr_employee_public_view_form`
- Name: hr.employee.public.form
- Model: `hr.employee.public`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `address_id`, `company_id`, `department_id`, `hr_icon_display`, `image_1920`, `job_id`, `mobile_phone`, `name`, `parent_id`, `show_hr_icon_display`, and 3 more
- XPath or positional patches: 0

### `hr_employee_public_view_search`
- Name: hr.employee.search
- Model: `hr.employee.public`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `company_id`, `department_id`, `job_id`, `name`, `parent_id`
- XPath or positional patches: 0

## Actions

- `act_hr_employee_public_form_view`: `view`
- `act_hr_employee_public_tree_view`: `view`
- `act_hr_employee_public_kanban_view`: `view`
- `hr_employee_public_action`: `act_window` Employees

## Navigation

- **Parent:** [[docs/Community Addons/hr/Views]]

<!-- GENERATED:VIEWFILE -->
