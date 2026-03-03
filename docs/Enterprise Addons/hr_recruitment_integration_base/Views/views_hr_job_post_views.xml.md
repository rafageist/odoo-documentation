---
tags: [odoo, enterprise, generated, views]
---

# views/hr_job_post_views.xml

- Module: [[docs/Enterprise Addons/hr_recruitment_integration_base/hr_recruitment_integration_base|hr_recruitment_integration_base]]
- Scope: Enterprise Addons
- Source file: `views/hr_job_post_views.xml`
- Views: 4
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `hr_job_post_view_kanban_search`
- Name: hr.job.post.kanban.search
- Model: `hr.job.post`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `apply_vector`, `job_id`, `platform_id`
- XPath or positional patches: 0

### `hr_job_post_view_kanban`
- Name: hr.job.post.kanban
- Model: `hr.job.post`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `campaign_end_date`, `campaign_start_date`, `create_uid`, `job_id`, `platform_icon`, `platform_id`, `status`
- Buttons: `action_post_job`
- XPath or positional patches: 0

### `hr_job_post_view_form`
- Name: hr.job.post.form
- Model: `hr.job.post`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `apply_method`, `apply_vector`, `campaign_end_date`, `campaign_start_date`, `job_id`, `platform_id`, `post_html`, `recruiter_id`, `status`
- Buttons: `action_post_now`, `action_update_job_post_check`
- XPath or positional patches: 0

### `hr_job_post_view_list`
- Name: hr.job.post.tree
- Model: `hr.job.post`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `apply_method`, `apply_vector`, `campaign_end_date`, `campaign_start_date`, `company_id`, `create_date`, `create_uid`, `job_id`, `platform_id`, `status`
- Buttons: `action_post_now`, `action_stop_campaign`
- XPath or positional patches: 0

## Actions

- `hr_job_post_double_check_action`: `server` Double Check Job Post
- `action_open_hr_job_post`: `act_window` Job Boards Posts

## Menus

- `menu_hr_job_boards`: Job Boards Posts

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_recruitment_integration_base/Views]]

