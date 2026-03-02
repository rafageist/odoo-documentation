<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_job_views.xml

- Module: [[docs/Community Addons/hr_recruitment_survey/hr_recruitment_survey|hr_recruitment_survey]]
- Scope: Community Addons
- Source file: `views/hr_job_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_hr_job_kanban_inherit`
- Name: hr.job.kanban.inherit
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_recruitment.view_hr_job_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `survey_id`
- XPath or positional patches: 3

### `hr_job_survey_inherit`
- Name: hr.job.form.inherit
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_job_survey`
- Root tag: `field`
- Field references: 2
- Sample fields: `interviewer_ids`, `survey_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment_survey/Views]]

<!-- GENERATED:VIEWFILE -->
