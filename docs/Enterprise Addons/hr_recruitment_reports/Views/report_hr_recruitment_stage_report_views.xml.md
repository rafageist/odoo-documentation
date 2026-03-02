<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/hr_recruitment_stage_report_views.xml

- Module: [[docs/Enterprise Addons/hr_recruitment_reports/hr_recruitment_reports|hr_recruitment_reports]]
- Scope: Enterprise Addons
- Source file: `report/hr_recruitment_stage_report_views.xml`
- Views: 6
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `hr_recruitment_report_inherit_kanban_view`
- Name: unnamed
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_recruitment.view_hr_job_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `recruitment_stage_report_view_search`
- Name: unnamed
- Model: `hr.recruitment.stage.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `company_id`, `date_begin`, `date_end`, `job_id`, `state`
- XPath or positional patches: 0

### `recruitment_stage_report_view_cohort`
- Name: unnamed
- Model: `hr.recruitment.stage.report`
- Type: inferred from arch
- Root tag: `cohort`
- Field references: 9
- Sample fields: `applicant_id`, `company_id`, `date_begin`, `date_end`, `days_in_stage`, `job_id`, `name`, `stage_id`, `state`
- XPath or positional patches: 0

### `recruitment_stage_report_view_pivot`
- Name: unnamed
- Model: `hr.recruitment.stage.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `days_in_stage`, `job_id`, `stage_id`
- XPath or positional patches: 0

### `recruitment_stage_report_view_graph`
- Name: unnamed
- Model: `hr.recruitment.stage.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `days_in_stage`, `job_id`, `stage_id`
- XPath or positional patches: 0

### `recruitment_stage_report_view_list`
- Name: unnamed
- Model: `hr.recruitment.stage.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `company_id`, `date_begin`, `date_end`, `days_in_stage`, `job_id`, `name`, `stage_id`, `state`
- XPath or positional patches: 0

## Actions

- `recruitment_stage_report_job_action`: `act_window` Time In Stage Analysis
- `recruitment_stage_report_action`: `act_window` Hiring Velocity

## Menus

- `hr_applicant_stage_report_menu`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_recruitment_reports/Views]]

<!-- GENERATED:VIEWFILE -->
