<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_views.xml

- Module: [[docs/Community Addons/hr_org_chart/hr_org_chart|hr_org_chart]]
- Scope: Community Addons
- Source file: `views/hr_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `hr_employee_hierarchy_view`
- Name: hr.employee.view.hierarchy
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `hierarchy`
- Field references: 7
- Sample fields: `department_color`, `department_id`, `hr_icon_display`, `image_1024`, `job_id`, `job_title`, `name`
- XPath or positional patches: 0

### `hr_employee_view_graph_inherit_org_chart`
- Name: hr.employee.view.graph.inherit.org_chart
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.hr_employee_view_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `department_color`
- XPath or positional patches: 1

### `hr_employee_view_pivot_inherit_org_chart`
- Name: hr.employee.view.pivot.inherit.org_chart
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.hr_employee_view_pivot`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `department_color`
- XPath or positional patches: 1

### `hr_employee_view_form_inherit_org_chart`
- Name: hr.employee.view.form.inherit.org_chart
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `div`
- Field references: 1
- Sample fields: `child_ids`
- XPath or positional patches: 1

## Actions

- `act_open_view_employee_list_my_hierarchy_view`: `view`
- `action_hr_employee_org_chart`: `act_window` Org Chart

## Navigation

- **Parent:** [[docs/Community Addons/hr_org_chart/Views]]

<!-- GENERATED:VIEWFILE -->
