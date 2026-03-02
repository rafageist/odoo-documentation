<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_job_views.xml

- Module: [[docs/Enterprise Addons/hr_recruitment_integration_base/hr_recruitment_integration_base|hr_recruitment_integration_base]]
- Scope: Enterprise Addons
- Source file: `views/hr_job_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_hr_job_kanban`
- Name: hr.job.kanban.inherit.hr.recruitment.integration.base
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_recruitment.view_hr_job_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `view_hr_job_form`
- Name: hr.job.form.inherit.hr.recruitment.integration.base
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr.view_hr_job_form`
- Root tag: `div`
- Field references: 13
- Sample fields: `apply_method`, `campaign_end_date`, `campaign_start_date`, `contract_type_id`, `expected_degree`, `job_post_count`, `job_post_ids`, `payment_interval`, `platform_id`, `salary_max`, and 3 more
- Buttons: `action_open_hr_job_post`, `action_post_job`
- XPath or positional patches: 3

## Actions

- `action_publish_on_job_board`: `server` Publish on Job Board

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_recruitment_integration_base/Views]]

<!-- GENERATED:VIEWFILE -->
