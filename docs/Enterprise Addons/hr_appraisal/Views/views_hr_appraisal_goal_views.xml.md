---
tags: [odoo, enterprise, generated, views]
---

# views/hr_appraisal_goal_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]]
- Scope: Enterprise Addons
- Source file: `views/hr_appraisal_goal_views.xml`
- Views: 7
- Actions: 3
- Menus: 2
- Rules: 0

## View records

### `hr_appraisal_goal_tag_view_tree`
- Name: hr.appraisal.goal.tag.view.list
- Model: `hr.appraisal.goal.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `color`, `name`
- XPath or positional patches: 0

### `hr_appraisal_goal_view_search`
- Name: hr.appraisal.goal.view.search
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `department_ids`, `job_ids`, `manager_ids`, `name`, `tag_ids`
- XPath or positional patches: 0

### `hr_appraisal_goal_view_hierarchy`
- Name: hr.appraisal.goal.view.hierarchy
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Root tag: `hierarchy`
- Field references: 4
- Sample fields: `deadline`, `name`, `progression`, `tag_ids`
- XPath or positional patches: 0

### `hr_appraisal_goal_view_graph`
- Name: hr.appraisal.goal.view.graph
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `employee_ids`, `progression`
- XPath or positional patches: 0

### `hr_appraisal_goal_view_kanban`
- Name: hr.appraisal.goal.view.kanban
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `activity_ids`, `deadline`, `employee_ids`, `name`, `progression`, `tag_ids`
- XPath or positional patches: 0

### `hr_appraisal_goal_view_tree`
- Name: hr.appraisal.goal.view.list
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `activity_ids`, `create_date`, `deadline`, `description`, `employee_ids`, `manager_ids`, `name`, `progression`, `tag_ids`
- XPath or positional patches: 0

### `hr_appraisal_goal_view_form`
- Name: hr.appraisal.goal.view.form
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `deadline`, `description`, `employee_ids`, `manager_ids`, `name`, `progression`, `sibling_goals_ratio`, `tag_ids`
- Buttons: `action_confirm`, `action_open_goal_template`, `action_save_as_template`
- XPath or positional patches: 0

## Actions

- `hr_appraisal_goal_tag_action`: `act_window` Goal Tags
- `action_hr_appraisal_goal_view_list`: `view`
- `action_hr_appraisal_goal`: `act_window` Goals

## Menus

- `menu_config_goal_tags`: Tags
- `menu_hr_appraisal_goal`: Goals

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal/Views]]

