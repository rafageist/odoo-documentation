<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_department_views.xml

- Module: [[docs/Community Addons/hr/hr|hr]]
- Scope: Community Addons
- Source file: `views/hr_department_views.xml`
- Views: 4
- Actions: 8
- Menus: 0
- Rules: 0

## View records

### `hr_department_view_kanban`
- Name: hr.department.kanban
- Model: `hr.department`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `active`, `color`, `company_id`, `manager_id`, `name`, `total_employee`
- Buttons: `action_employee_from_department`
- XPath or positional patches: 0

### `view_department_filter`
- Name: hr.department.search
- Model: `hr.department`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `manager_id`, `name`
- XPath or positional patches: 0

### `view_department_tree`
- Name: hr.department.list
- Model: `hr.department`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `color`, `company_id`, `manager_id`, `name`, `parent_id`, `total_employee`
- XPath or positional patches: 0

### `view_department_form`
- Name: hr.department.form
- Model: `hr.department`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `active`, `child_ids`, `color`, `company_id`, `manager_id`, `name`, `parent_id`, `plans_count`, `total_employee`
- Buttons: `action_employee_from_department`, `action_plan_from_department`
- XPath or positional patches: 0

## Actions

- `hr_department_form_view_kanban_action`: `view`
- `hr_department_tree_view_kanban_action`: `view`
- `hr_department_kanban_view_kanban_action`: `view`
- `hr_department_kanban_action`: `act_window` Departments
- `hr_department_kanban_view_tree_action`: `view`
- `hr_department_form_view_tree_action`: `view`
- `hr_department_tree_view_tree_action`: `view`
- `hr_department_tree_action`: `act_window` Departments

## Navigation

- **Parent:** [[docs/Community Addons/hr/Views]]

<!-- GENERATED:VIEWFILE -->
