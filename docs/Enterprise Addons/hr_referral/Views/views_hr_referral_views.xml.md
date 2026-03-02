<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_referral_views.xml

- Module: [[docs/Enterprise Addons/hr_referral/hr_referral|hr_referral]]
- Scope: Enterprise Addons
- Source file: `views/hr_referral_views.xml`
- Views: 4
- Actions: 2
- Menus: 3
- Rules: 0

## View records

### `view_hr_referral_points_form`
- Name: hr.referral.points.form
- Model: `hr.referral.points`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `applicant_id`, `company_id`, `hr_referral_reward_id`, `points`, `ref_user_id`, `sequence_stage`, `stage_id`
- XPath or positional patches: 0

### `view_hr_referral_gift_tree`
- Name: hr.referral.points.list
- Model: `hr.referral.points`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `hr_referral_reward_id`, `points`, `ref_user_id`
- XPath or positional patches: 0

### `view_hr_referral_points_tree`
- Name: hr.referral.points.list
- Model: `hr.referral.points`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `applicant_id`, `applicant_name`, `company_id`, `hr_referral_reward_id`, `points`, `ref_user_id`, `stage_id`, `write_date`
- XPath or positional patches: 0

### `view_hr_referral_points_filter`
- Name: hr.referral.points.filter
- Model: `hr.referral.points`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `ref_user_id`
- XPath or positional patches: 0

## Actions

- `action_hr_referral_welcome_screen`: `client` Dashboard
- `action_hr_referral_points`: `act_window` Points

## Menus

- `menu_hr_points_referral`: unnamed
- `menu_hr_referral_reporting`: Reporting
- `menu_hr_applicant_employee_referral_dashboard`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_referral/Views]]

<!-- GENERATED:VIEWFILE -->
