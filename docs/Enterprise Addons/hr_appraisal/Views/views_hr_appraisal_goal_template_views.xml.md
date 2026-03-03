---
tags: [odoo, enterprise, generated, views]
---

# views/hr_appraisal_goal_template_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]]
- Scope: Enterprise Addons
- Source file: `views/hr_appraisal_goal_template_views.xml`
- Views: 5
- Actions: 3
- Menus: 2
- Rules: 0

## View records

### `hr_appraisal_goal_template_library_view_list`
- Name: hr.appraisal.goal.template.view.list
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Inherits: `hr_appraisal.hr_appraisal_goal_template_view_list`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `hr_appraisal_goal_template_view_search`
- Name: hr.appraisal.goal.template.view.search
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `name`, `parent_id`, `tag_ids`
- XPath or positional patches: 0

### `hr_appraisal_goal_template_view_hierarchy`
- Name: hr.appraisal.goal.template.view.hierarchy
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Root tag: `hierarchy`
- Field references: 4
- Sample fields: `deadline`, `name`, `tag_ids`, `usual_duration_month`
- XPath or positional patches: 0

### `hr_appraisal_goal_template_view_list`
- Name: hr.appraisal.goal.template.view.list
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `child_ids`, `name`, `tag_ids`
- XPath or positional patches: 0

### `hr_appraisal_goal_template_view_form`
- Name: hr.appraisal.goal.template.view.form
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `active`, `child_ids`, `description`, `name`, `parent_id`, `tag_ids`, `usual_duration_month`
- XPath or positional patches: 0

## Actions

- `act_hr_appraisal_goal_template_library_list`: `view`
- `action_hr_appraisal_goal_template_library`: `act_window` Goals Template Library
- `action_hr_appraisal_goal_template`: `act_window` Goals Template

## Menus

- `menu_config_goal_template`: Library
- `menu_config_goal`: Goals

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal/Views]]

