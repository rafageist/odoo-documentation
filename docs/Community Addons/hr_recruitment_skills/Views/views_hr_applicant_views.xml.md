<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_applicant_views.xml

- Module: [[docs/Community Addons/hr_recruitment_skills/hr_recruitment_skills|hr_recruitment_skills]]
- Scope: Community Addons
- Source file: `views/hr_applicant_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `crm_case_tree_view_inherit_hr_recruitment_skills`
- Name: hr.applicant.view.tree.inherit.skills
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment_skills.crm_case_tree_view_job`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `application_status`, `categ_ids`, `matching_skill_ids`, `missing_skill_ids`, `partner_name`, `partner_phone`, `priority`
- Buttons: `action_add_to_job`
- XPath or positional patches: 3

### `crm_case_tree_view_job`
- Name: hr.applicant.view.list.inherit.hr.recruitment.skills
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.crm_case_tree_view_job`
- Root tag: `field`
- Field references: 2
- Sample fields: `matching_score`, `stage_id`
- XPath or positional patches: 0

### `hr_applicant_view_search`
- Name: hr.applicant.view.search.inherit.skills
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_applicant_view_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `applicant_skill_ids`
- XPath or positional patches: 2

### `hr_applicant_view_search_bis`
- Name: hr.applicant.view.search.inherit.skills.bis
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_applicant_view_search_bis`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `applicant_skill_ids`
- XPath or positional patches: 1

### `hr_applicant_view_form`
- Name: hr.applicant.view.form.inherit.hr.recruitment.skills
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_applicant_view_form`
- Root tag: `notebook`
- Field references: 8
- Sample fields: `current_applicant_skill_ids`, `id`, `level_progress`, `matching_score`, `skill_id`, `skill_level_id`, `skill_type_id`, `valid_to`
- XPath or positional patches: 1

## Actions

- `action_find_matching_job`: `act_window` Matching Positions

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment_skills/Views]]

<!-- GENERATED:VIEWFILE -->
