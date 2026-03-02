<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_employee_public_views.xml

- Module: [[docs/Community Addons/hr_org_chart/hr_org_chart|hr_org_chart]]
- Scope: Community Addons
- Source file: `views/hr_employee_public_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `hr_employee_public_view_form_inherit_org_chart`
- Name: hr.employee.public.view.form.inherit.org_chart
- Model: `hr.employee.public`
- Type: inferred from arch
- Inherits: `hr.hr_employee_public_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `child_ids`
- XPath or positional patches: 1

### `hr_employee_public_hierarchy_view`
- Name: hr.employee.public.hierarchy.view
- Model: `hr.employee.public`
- Type: inferred from arch
- Root tag: `hierarchy`
- Field references: 6
- Sample fields: `department_color`, `department_id`, `hr_icon_display`, `image_1024`, `job_id`, `name`
- XPath or positional patches: 0

## Actions

- `act_hr_employee_public_hierarchy_view`: `view`
- `action_hr_employee_public_org_chart`: `act_window` Org Chart

## Navigation

- **Parent:** [[docs/Community Addons/hr_org_chart/Views]]

<!-- GENERATED:VIEWFILE -->
