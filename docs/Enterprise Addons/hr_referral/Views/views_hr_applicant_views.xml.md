<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_applicant_views.xml

- Module: [[docs/Enterprise Addons/hr_referral/hr_referral|hr_referral]]
- Scope: Enterprise Addons
- Source file: `views/hr_applicant_views.xml`
- Views: 4
- Actions: 4
- Menus: 2
- Rules: 0

## View records

### `view_hr_referral_filter`
- Name: hr.referral.filter
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 0

### `view_hr_applicant_employee_referral_kanban`
- Name: hr.applicant.employee.referral.kanban
- Model: `hr.applicant`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `earned_points`, `friend_id`, `job_id`, `max_points`, `partner_name`, `referral_state`, `shared_item_infos`, `user_id`
- XPath or positional patches: 0

### `hr_applicant_view_search_bis_inherit_referral`
- Name: hr.applicant.view.search.inherit.referral
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_applicant_view_search_bis`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `ref_user_id`
- XPath or positional patches: 2

### `hr_applicant_view_form_inherit_referral`
- Name: hr.applicant.view.form.inherit.referral
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_applicant_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `is_accessible_to_current_user`, `ref_user_id`
- XPath or positional patches: 1

## Actions

- `action_hr_refused_applicant_employee_referral`: `act_window` My Referral
- `action_hr_applicant_employee_referral`: `act_window` My Referral
- `hr_recruitment.action_hr_job_applications`: `act_window`
- `hr_recruitment.crm_case_categ0_act_job`: `act_window`

## Menus

- `menu_hr_referral_configuration`: Configuration
- `menu_hr_referral_root`: Referrals

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_referral/Views]]

<!-- GENERATED:VIEWFILE -->
