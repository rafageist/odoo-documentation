---
tags: [odoo, enterprise, generated, views]
---

# report/hr_referral_report_views.xml

- Module: [[docs/Enterprise Addons/hr_referral/hr_referral|hr_referral]]
- Scope: Enterprise Addons
- Source file: `report/hr_referral_report_views.xml`
- Views: 5
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `employee_referral_report_view_search`
- Name: employee.referral.report.view.search
- Model: `hr.referral.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `department_id`, `job_id`, `medium_id`, `ref_user_id`, `write_date`
- XPath or positional patches: 0

### `hr_referral_report_view_tree`
- Name: hr.referral.report.view.list
- Model: `hr.referral.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `applicant_id`, `company_id`, `department_id`, `job_id`, `medium_id`, `ref_user_id`, `referral_state`
- XPath or positional patches: 0

### `hr_referral_report_view_form`
- Name: hr.referral.report.view.form
- Model: `hr.referral.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `applicant_id`, `company_id`, `department_id`, `job_id`, `medium_id`, `ref_user_id`, `referral_state`
- XPath or positional patches: 0

### `employee_referral_report_view_graph`
- Name: employee.referral.report.view.graph
- Model: `hr.referral.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `applicant_id`, `medium_id`, `referral_state`
- XPath or positional patches: 0

### `employee_referral_report_view_pivot`
- Name: employee.referral.report.view.pivot
- Model: `hr.referral.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `applicant_id`, `earned_points`, `employee_referral_hired`, `employee_referral_refused`, `ref_user_id`
- XPath or positional patches: 0

## Actions

- `employee_referral_report_action`: `act_window` Employees Referral Analysis

## Menus

- `menu_report_employee_referral_all`: Referral Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_referral/Views]]

