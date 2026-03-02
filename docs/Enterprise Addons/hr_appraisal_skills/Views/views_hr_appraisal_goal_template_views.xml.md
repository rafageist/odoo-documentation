<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_appraisal_goal_template_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal_skills/hr_appraisal_skills|hr_appraisal_skills]]
- Scope: Enterprise Addons
- Source file: `views/hr_appraisal_goal_template_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_appraisal_goal_template_view_tree`
- Name: hr.appraisal.goal.template.view.list.inherit.hr_appraisal_skills
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Inherits: `hr_appraisal.hr_appraisal_goal_template_view_list`
- Root tag: `field`
- Field references: 2
- Sample fields: `child_ids`, `current_goal_skill_ids`
- XPath or positional patches: 0

### `hr_appraisal_goal_template_view_hierarchy`
- Name: hr.appraisal.goal.template.view.hierarchy.inherit.hr_appraisal_skills
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Inherits: `hr_appraisal.hr_appraisal_goal_template_view_hierarchy`
- Root tag: `span`
- Field references: 1
- Sample fields: `current_goal_skill_ids`
- XPath or positional patches: 1

### `hr_appraisal_goal_template_view_form`
- Name: hr.appraisal.goal.template.view.form.inherit.hr_appraisal_skills
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Inherits: `hr_appraisal.hr_appraisal_goal_template_view_form`
- Root tag: `group`
- Field references: 5
- Sample fields: `color`, `current_goal_skill_ids`, `display_name`, `skill_id`, `skill_level_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal_skills/Views]]

<!-- GENERATED:VIEWFILE -->
