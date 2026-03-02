<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_applicant_views.xml

- Module: [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]
- Scope: Community Addons
- Source file: `views/hr_applicant_views.xml`
- Views: 15
- Actions: 15
- Menus: 0
- Rules: 0

## View records

### `hr_applicant_view_search`
- Name: hr.applicant.search
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `search`
- Field references: 8
- Sample fields: `company_id`, `create_date`, `date_closed`, `department_id`, `job_id`, `priority`, `stage_id`, `user_id`
- XPath or positional patches: 0

### `hr_applicant_view_graph`
- Name: hr.applicant.graph
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `job_id`, `stage_id`
- XPath or positional patches: 0

### `hr_applicant_view_pivot`
- Name: hr.applicant.pivot
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `job_id`, `partner_name`, `stage_id`
- XPath or positional patches: 0

### `hr_kanban_view_applicant_talent_pool`
- Name: unnamed
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_kanban_view_applicant`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `hr_applicant_view_activity`
- Name: hr.applicant.activity
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 2
- Sample fields: `partner_name`, `user_id`
- XPath or positional patches: 0

### `hr_kanban_view_applicant`
- Name: Hr Applicants kanban
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 21
- Sample fields: `active`, `activity_ids`, `applicant_properties`, `application_status`, `attachment_number`, `categ_ids`, `color`, `company_id`, `date_closed`, `is_rotting`, and 11 more
- Buttons: `action_talent_pool_add_applicants`
- XPath or positional patches: 0

### `quick_create_applicant_form`
- Name: hr.applicant.form.quick_create
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `company_id`, `job_id`, `partner_name`
- XPath or positional patches: 0

### `hr_applicant_calendar_view`
- Name: Hr Applicants Calendar
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 5
- Sample fields: `activity_summary`, `job_id`, `partner_name`, `priority`, `user_id`
- XPath or positional patches: 0

### `hr_applicant_view_search_bis`
- Name: hr.applicant.view.search
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `search`
- Field references: 14
- Sample fields: `activity_type_id`, `activity_user_id`, `application_status`, `attachment_ids`, `categ_ids`, `company_id`, `date_closed`, `department_id`, `email_from`, `job_id`, and 4 more
- XPath or positional patches: 0

### `crm_case_graph_view_job`
- Name: Jobs - Recruitment Graph
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `stage_id`
- XPath or positional patches: 0

### `crm_case_pivot_view_job`
- Name: Jobs - Recruitment
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `color`, `job_id`, `stage_id`
- XPath or positional patches: 0

### `hr_applicant_view_form_interviewer`
- Name: unnamed
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_applicant_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `hr_applicant_view_form`
- Name: Jobs - Recruitment Form
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `form`
- Field references: 46
- Sample fields: `active`, `applicant_notes`, `applicant_properties`, `application_count`, `application_status`, `availability`, `campaign_id`, `categ_ids`, `company_id`, `date_closed`, and 36 more
- Buttons: `action_create_meeting`, `action_job_add_applicants`, `action_open_applications`, `action_open_employee`, `action_talent_pool_add_applicants`, `action_talent_pool_stat_button`, `action_unarchive`, `archive_applicant`, `create_employee_from_applicant`
- XPath or positional patches: 0

### `hr_applicant_view_tree_activity`
- Name: hr.applicant.view.list.activity
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `activity_date_deadline`, `activity_exception_decoration`, `activity_summary`, `activity_type_id`, `partner_id`, `stage_id`
- XPath or positional patches: 0

### `crm_case_tree_view_job`
- Name: Applicants
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `list`
- Field references: 27
- Sample fields: `activity_date_deadline`, `activity_ids`, `application_status`, `availability`, `categ_ids`, `company_id`, `create_date`, `date_last_stage_update`, `department_id`, `email_from`, and 17 more
- Buttons: `action_job_add_applicants`, `action_talent_pool_add_applicants`, `archive_applicant`
- XPath or positional patches: 0

## Actions

- `mail_followers_edit_action_from_hr_recruitment`: `act_window` Add/Remove Followers
- `action_applicant_send_mail`: `server` Send Email
- `action_hr_recruitment_report_filtered_job`: `act_window` Recruitment Analysis
- `action_hr_recruitment_report_filtered_department`: `act_window` Recruitment Analysis
- `hr_applicant_action_analysis`: `act_window` Recruitment Analysis
- `action_hr_sec_graph_view_act_job`: `view`
- `hr_applicant_action_view_pivot`: `view`
- `action_hr_sec_form_view_act_job`: `view`
- `action_hr_sec_tree_view_act_job`: `view`
- `action_hr_sec_kanban_view_act_job`: `view`
- `hr_applicant_action_from_department`: `act_window` New Applications
- `crm_case_categ0_act_job`: `act_window` Applications
- `action_hr_applicant_new`: `act_window`
- `action_hr_talent_pool_applications`: `act_window` Talents
- `action_hr_job_applications`: `act_window` Applications

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment/Views]]

<!-- GENERATED:VIEWFILE -->
