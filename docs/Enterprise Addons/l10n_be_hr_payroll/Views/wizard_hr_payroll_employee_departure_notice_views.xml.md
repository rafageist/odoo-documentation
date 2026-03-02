<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# wizard/hr_payroll_employee_departure_notice_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `wizard/hr_payroll_employee_departure_notice_views.xml`
- Views: 1
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `view_hr_payroll_employee_departure_notice`
- Name: hr_payroll_employee_departure_notice
- Model: `hr.payslip.employee.depature.notice`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `actual_notice_duration`, `departure_date`, `departure_description`, `employee_id`, `end_notice_period`, `first_contract`, `l10n_be_scale_seniority`, `leaving_type_id`, `notice_duration_month_before_2014`, `notice_duration_week_after_2014`, and 6 more
- Buttons: `compute_termination_fee`, `validate_termination`
- XPath or positional patches: 0

## Actions

- `departure_notice_wizard_action`: `act_window` Departure: Notice period and payslip

## Menus

- `menu_l10n_be_hr_payroll_notice`: Departure: Notice period
- `menu_reporting_l10n_be`: Belgium

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
