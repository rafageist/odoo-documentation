---
tags: [odoo, enterprise, generated, views]
---

# report/hr_appraisal_skill_report_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal_skills/hr_appraisal_skills|hr_appraisal_skills]]
- Scope: Enterprise Addons
- Source file: `report/hr_appraisal_skill_report_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `hr_appraisal_skill_report_view_search`
- Name: unnamed
- Model: `hr.appraisal.skill.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `department_id`, `employee_id`, `skill_id`, `skill_type_id`
- XPath or positional patches: 0

### `hr_appraisal_skill_report_view_pivot`
- Name: hr.appraisal.skill.report.view.pivot
- Model: `hr.appraisal.skill.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 7
- Sample fields: `current_level_progress`, `current_skill_level_id`, `employee_id`, `previous_level_progress`, `previous_skill_level_id`, `skill_id`, `skill_type_id`
- XPath or positional patches: 0

### `hr_appraisal_skill_report_view_graph`
- Name: hr.appraisal.skill.report.view.graph
- Model: `hr.appraisal.skill.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `employee_id`, `progress_evolution`, `skill_type_id`
- XPath or positional patches: 0

### `hr_appraisal_skill_report_view_tree`
- Name: unnamed
- Model: `hr.appraisal.skill.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `current_level_progress`, `current_skill_level_id`, `employee_id`, `evolution`, `justification`, `previous_level_progress`, `previous_skill_level_id`, `progress_evolution`, `skill_id`, `skill_type_id`
- XPath or positional patches: 0

## Actions

- `hr_appraisal_skill_report_action`: `act_window` Appraisal Skills Report

## Menus

- `menu_appraisal_skills_report`: Skills Evolution

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal_skills/Views]]

