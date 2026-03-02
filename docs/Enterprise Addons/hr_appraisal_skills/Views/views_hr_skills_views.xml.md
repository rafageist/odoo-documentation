<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_skills_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal_skills/hr_appraisal_skills|hr_appraisal_skills]]
- Scope: Enterprise Addons
- Source file: `views/hr_skills_views.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_hr_appraisal_form`
- Name: hr.appraisal.form.inherit.hr_appraisal_skills
- Model: `hr.appraisal`
- Type: inferred from arch
- Inherits: `hr_appraisal.view_hr_appraisal_form`
- Root tag: `field`
- Field references: 12
- Sample fields: `current_appraisal_skill_ids`, `goals_completion_percentage`, `job_id`, `justification`, `level_progress`, `skill_id`, `skill_level_id`, `skill_type_id`, `target_job_id`, `target_job_skill_progress`, and 2 more
- Buttons: `action_open_recommend_goals`
- XPath or positional patches: 1

## Actions

- `hr_skill_type_action_appraisal`: `act_window` Skills Type

## Menus

- `menu_hr_appraisal_surveys`: Skills

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal_skills/Views]]

<!-- GENERATED:VIEWFILE -->
