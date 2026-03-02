<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_department_views.xml

- Module: [[docs/Community Addons/hr_org_chart/hr_org_chart|hr_org_chart]]
- Scope: Community Addons
- Source file: `views/hr_department_views.xml`
- Views: 1
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `hr_department_hierarchy_view`
- Name: hr.departmnent.view.hierarchy
- Model: `hr.department`
- Type: inferred from arch
- Root tag: `hierarchy`
- Field references: 4
- Sample fields: `color`, `manager_id`, `name`, `total_employee`
- Buttons: `action_employee_from_department`
- XPath or positional patches: 0

## Actions

- `act_hr_department_hierarchy_view_tree_action`: `view`
- `act_hr_department_hierarchy_view_kanban_action`: `view`

## Navigation

- **Parent:** [[docs/Community Addons/hr_org_chart/Views]]

<!-- GENERATED:VIEWFILE -->
