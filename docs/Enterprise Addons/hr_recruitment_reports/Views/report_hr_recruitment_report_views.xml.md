<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/hr_recruitment_report_views.xml

- Module: [[docs/Enterprise Addons/hr_recruitment_reports/hr_recruitment_reports|hr_recruitment_reports]]
- Scope: Enterprise Addons
- Source file: `report/hr_recruitment_report_views.xml`
- Views: 9
- Actions: 5
- Menus: 3
- Rules: 0

## View records

### `recruitment_report_team_view_pivot`
- Name: unnamed
- Model: `hr.recruitment.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `count`, `hired`, `in_progress`, `refused`, `user_id`
- XPath or positional patches: 0

### `recruitment_report_team_view_graph`
- Name: unnamed
- Model: `hr.recruitment.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `state`, `user_id`
- XPath or positional patches: 0

### `recruitment_report_view_search`
- Name: hr.recruitment.report.search
- Model: `hr.recruitment.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `company_id`, `create_date`, `date_closed`, `job_id`, `name`, `refuse_reason_id`, `source_id`
- XPath or positional patches: 0

### `hr_recruitment_report_view_tree`
- Name: hr.recruitment.report.view.list
- Model: `hr.recruitment.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `create_date`, `job_id`, `medium_id`, `name`, `source_id`, `stage_id`, `state`
- XPath or positional patches: 0

### `recruitment_report_hr_recruitment_view_graph`
- Name: hr.recruitment.report.view.graph
- Model: `hr.recruitment.report`
- Type: inferred from arch
- Inherits: `hr_recruitment_reports.recruitment_report_source_view_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `create_date`
- XPath or positional patches: 2

### `recruitment_report_source_view_graph`
- Name: unnamed
- Model: `hr.recruitment.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `count`, `source_id`, `state`
- XPath or positional patches: 0

### `recruitment_report_view_graph`
- Name: hr.recruitment.report.graph
- Model: `hr.recruitment.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `count`, `create_date`
- XPath or positional patches: 0

### `recruitment_report_view_source_pivot`
- Name: unnamed
- Model: `hr.recruitment.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `count`, `hired`, `in_progress`, `refused`, `source_id`
- XPath or positional patches: 0

### `recruitment_report_view_pivot`
- Name: hr.recruitment.report.pivot
- Model: `hr.recruitment.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 7
- Sample fields: `count`, `create_date`, `hired`, `in_progress`, `job_id`, `refused`, `stage_id`
- XPath or positional patches: 0

## Actions

- `recruitment_report_team_action`: `act_window` Team Performance
- `recruitment_report_source_job_action`: `act_window` Source Analysis
- `recruitment_report_source_action`: `act_window` Source Analysis
- `recruitment_report_job_action`: `act_window` Recruitment Analysis
- `recruitment_report_action`: `act_window` Application Analysis

## Menus

- `hr_applicant_report_team_menu`: unnamed
- `hr_applicant_report_source_menu`: unnamed
- `hr_recruitment.hr_applicant_report_menu`: Application Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_recruitment_reports/Views]]

<!-- GENERATED:VIEWFILE -->
