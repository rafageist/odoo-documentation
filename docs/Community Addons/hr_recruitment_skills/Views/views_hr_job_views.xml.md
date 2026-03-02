<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_job_views.xml

- Module: [[docs/Community Addons/hr_recruitment_skills/hr_recruitment_skills|hr_recruitment_skills]]
- Scope: Community Addons
- Source file: `views/hr_job_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_hr_job_form`
- Name: hr.job.view.form.inherit.hr.recruitment.skills
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_skills.view_hr_job_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `hr_job_list_inherit_hr_recruitment_skills`
- Name: hr.job.view.list.inherit
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_job_view_tree_inherit`
- Root tag: `field`
- Field references: 2
- Sample fields: `applicant_matching_score`, `department_id`
- XPath or positional patches: 0

## Actions

- `action_applicant_search_applicant`: `server` Search Matching Applicants

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment_skills/Views]]

<!-- GENERATED:VIEWFILE -->
