---
tags: [odoo, enterprise, generated, views]
---

# views/hr_appraisal_goal_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal_skills/hr_appraisal_skills|hr_appraisal_skills]]
- Scope: Enterprise Addons
- Source file: `views/hr_appraisal_goal_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_appraisal_goal_view_tree`
- Name: hr.appraisal.goal.view.list.inherit.hr.appraisal.skills
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Inherits: `hr_appraisal.hr_appraisal_goal_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `current_goal_skill_ids`, `tag_ids`
- XPath or positional patches: 0

### `hr_appraisal_goal_view_hierarchy`
- Name: hr.appraisal.goal.view.hierarchy.inherit.hr_appraisal_skills
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Inherits: `hr_appraisal.hr_appraisal_goal_view_hierarchy`
- Root tag: `span`
- Field references: 1
- Sample fields: `current_goal_skill_ids`
- XPath or positional patches: 1

### `hr_appraisal_goal_view_search`
- Name: hr.appraisal.goal.view.search.inherit.hr.appraisal.skills
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Inherits: `hr_appraisal.hr_appraisal_goal_view_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `current_goal_skill_ids`, `tag_ids`
- XPath or positional patches: 0

### `hr_appraisal_goal_view_form`
- Name: hr.appraisal.goal.view.form.inherit.hr.appraisal.skills
- Model: `hr.appraisal.goal`
- Type: inferred from arch
- Inherits: `hr_appraisal.hr_appraisal_goal_view_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `current_goal_skill_ids`, `progression`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal_skills/Views]]

