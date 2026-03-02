<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_applicant_views.xml

- Module: [[docs/Community Addons/hr_recruitment_survey/hr_recruitment_survey|hr_recruitment_survey]]
- Scope: Community Addons
- Source file: `views/hr_applicant_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_kanban_view_applicant_inherit`
- Name: hr.applicants.kanban.inherit
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_kanban_view_applicant`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `survey_id`
- XPath or positional patches: 1

### `hr_applicant_view_form_inherit`
- Name: hr.applicant.form.inherit
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_applicant_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `response_ids`, `survey_id`
- Buttons: `action_print_survey`, `action_send_survey`
- XPath or positional patches: 3

### `crm_case_tree_view_job_inherit`
- Name: hr.applicant.list.inherit
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.crm_case_tree_view_job`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `response_ids`, `survey_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment_survey/Views]]

<!-- GENERATED:VIEWFILE -->
