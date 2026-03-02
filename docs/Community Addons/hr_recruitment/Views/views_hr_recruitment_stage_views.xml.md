<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_recruitment_stage_views.xml

- Module: [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]
- Scope: Community Addons
- Source file: `views/hr_recruitment_stage_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `hr_recruitment_stage_form`
- Name: hr.recruitment.stage.form
- Model: `hr.recruitment.stage`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `fold`, `hired_stage`, `is_warning_visible`, `job_ids`, `legend_blocked`, `legend_done`, `legend_normal`, `legend_waiting`, `name`, `requirements`, and 3 more
- XPath or positional patches: 0

### `view_hr_recruitment_stage_kanban`
- Name: hr.recruitment.stage.kanban
- Model: `hr.recruitment.stage`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `fold`, `name`
- XPath or positional patches: 0

### `hr_recruitment_stage_tree`
- Name: hr.recruitment.stage.list
- Model: `hr.recruitment.stage`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `fold`, `hired_stage`, `name`, `rotting_threshold_days`, `sequence`
- XPath or positional patches: 0

## Actions

- `hr_recruitment_stage_act`: `act_window` Stages
- `hr_job_stage_act`: `act_window` Recruitment / Applicants Stages

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment/Views]]

<!-- GENERATED:VIEWFILE -->
