<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_job_views.xml

- Module: [[docs/Enterprise Addons/hr_referral/hr_referral|hr_referral]]
- Scope: Enterprise Addons
- Source file: `views/hr_job_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `hr_job_form_inherit_hr_referral`
- Name: hr.job.view.form.inherit
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr.view_hr_job_form`
- Root tag: `header`
- Field references: 0
- Buttons: `action_referral_campaign`
- XPath or positional patches: 1

### `view_job_filter_referral`
- Name: hr.referral.job.search
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `website_hr_recruitment.hr_job_search_view_inherit`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `view_hr_job_kanban_inherit_referral`
- Name: hr.job.kanban.referral
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_recruitment.view_hr_job_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_hr_job_employee_referral_kanban`
- Name: hr.job.employee.referral.kanban
- Model: `hr.job`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `description`, `facebook_clicks`, `id`, `linkedin_clicks`, `max_points`, `name`, `no_of_recruitment`, `twitter_clicks`, `website_url`
- XPath or positional patches: 0

## Actions

- `action_hr_job_employee_referral`: `act_window` Job Positions

## Menus

- `menu_hr_referral_job_configuration`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_referral/Views]]

<!-- GENERATED:VIEWFILE -->
