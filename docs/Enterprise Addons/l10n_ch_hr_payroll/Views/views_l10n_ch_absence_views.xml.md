---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_absence_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_absence_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_ch_hr_leave_employee_view_dashboard`
- Name: hr.leave.view.dashboard
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 6
- Sample fields: `can_cancel`, `display_name`, `holiday_status_id`, `is_hatched`, `is_striked`, `state`
- XPath or positional patches: 0

### `l10n_ch_hr_leave_view_form`
- Name: hr.leave.view.form
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_view_form`
- Root tag: `field`
- Field references: 7
- Sample fields: `l10n_ch_continued_pay_percentage`, `l10n_ch_disability_percentage`, `l10n_ch_lpp_interruption`, `l10n_ch_pay_interruption`, `l10n_ch_swissdec_payroll_impact`, `l10n_ch_swissdec_work_interruption`, `name`
- XPath or positional patches: 0

### `l10n_ch_absence_leave_view_form`
- Name: hr.leave.view.form
- Model: `hr.leave`
- Type: inferred from arch
- Root tag: `form`
- Field references: 24
- Sample fields: `can_approve`, `can_cancel`, `date_from`, `date_to`, `employee_company_id`, `employee_id`, `has_mandatory_day`, `holiday_status_id`, `l10n_ch_continued_pay_percentage`, `l10n_ch_disability_percentage`, and 14 more
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

