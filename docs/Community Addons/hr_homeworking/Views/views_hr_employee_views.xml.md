<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Community Addons/hr_homeworking/hr_homeworking|hr_homeworking]]
- Scope: Community Addons
- Source file: `views/hr_employee_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_employee_tree`
- Name: hr.employee.list.timesheet
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `work_location_name`
- XPath or positional patches: 2

### `view_employee_form`
- Name: view.employee.form.inherit.hr
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `friday_location_id`, `monday_location_id`, `saturday_location_id`, `sunday_location_id`, `thursday_location_id`, `tuesday_location_id`, `wednesday_location_id`
- XPath or positional patches: 1

### `view_employee_filter`
- Name: view.employee.form.inherit.hr
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/hr_homeworking/Views]]

<!-- GENERATED:VIEWFILE -->
