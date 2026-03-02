<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_job_views.xml

- Module: [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]
- Scope: Community Addons
- Source file: `views/hr_job_views.xml`
- Views: 8
- Actions: 7
- Menus: 0
- Rules: 0

## View records

### `hr_job_platform_tree`
- Name: hr.job.platform.list
- Model: `hr.job.platform`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `email`, `name`, `regex`
- XPath or positional patches: 0

### `hr_job_platform_form`
- Name: hr.job.platform.form
- Model: `hr.job.platform`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `email`, `name`, `regex`
- XPath or positional patches: 0

### `hr_job_view_tree_inherit`
- Name: unnamed
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr.view_hr_job_tree`
- Root tag: `field`
- Field references: 13
- Sample fields: `alias_id`, `alias_name`, `allowed_user_ids`, `company_id`, `department_id`, `expected_employees`, `message_needaction`, `name`, `no_of_employee`, `no_of_hired_employee`, and 3 more
- XPath or positional patches: 1

### `hr_job_search_view`
- Name: hr.job.search
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_recruitment.view_job_filter_recruitment`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `company_id`, `department_id`
- XPath or positional patches: 1

### `hr_job_survey`
- Name: hr.job.form1
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr.view_hr_job_form`
- Root tag: `xpath`
- Field references: 11
- Sample fields: `address_id`, `alias_domain_id`, `alias_name`, `all_application_count`, `documents_count`, `employee_count`, `expected_degree`, `interviewer_ids`, `is_favorite`, `job_properties`, and 1 more
- Buttons: `%(action_hr_job_applications)d`, `action_open_attachments`, `action_open_employees`
- XPath or positional patches: 12

### `hr_job_simple_form`
- Name: hr.job.simple.form
- Model: `hr.job`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `alias_domain_id`, `alias_id`, `alias_name`, `name`
- Buttons: `%(action_hr_job_applications)d`
- XPath or positional patches: 0

### `view_job_filter_recruitment`
- Name: Job
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr.view_job_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_hr_job_kanban`
- Name: hr.job.kanban
- Model: `hr.job`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 14
- Sample fields: `active`, `activity_count`, `alias_email`, `alias_id`, `allowed_user_ids`, `application_count`, `color`, `company_id`, `is_favorite`, `name`, and 4 more
- Buttons: `%(action_hr_job_applications)d`, `action_open_activities`
- XPath or positional patches: 0

## Actions

- `action_hr_job_platforms`: `act_window` Emails
- `action_hr_job_interviewer`: `act_window` Job Positions
- `action_hr_job`: `act_window` Job Positions
- `action_load_demo_data`: `server` Load demo data
- `action_hr_job_config`: `act_window` Job Positions
- `create_job_simple`: `act_window` Create a Job Position
- `action_hr_job_new_application`: `act_window` New Application

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment/Views]]

<!-- GENERATED:VIEWFILE -->
