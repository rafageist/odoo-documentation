<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# wizard/hr_payroll_employee_departure_holiday_attest_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `wizard/hr_payroll_employee_departure_holiday_attest_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_hr_payroll_employee_departure_holiday_attests_n1_payslips`
- Name: view_hr_payroll_employee_departure_holiday_attests_n1_payslips
- Model: `hr.payslip.employee.depature.holiday.attests`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `basic_wage`, `currency_id`, `date_from`, `date_to`, `gross_wage`, `line_ids`, `net_wage`, `payslip_n1_ids`, `payslip_run_id`, `state`
- XPath or positional patches: 0

### `view_hr_payroll_employee_departure_holiday_attests_n_payslips`
- Name: view_hr_payroll_employee_departure_holiday_attests_n_payslips
- Model: `hr.payslip.employee.depature.holiday.attests`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `basic_wage`, `currency_id`, `date_from`, `date_to`, `gross_wage`, `line_ids`, `net_wage`, `payslip_n_ids`, `payslip_run_id`, `state`
- XPath or positional patches: 0

### `view_hr_payroll_employee_departure_holiday_attests`
- Name: view_hr_payroll_employee_departure_holiday_attests
- Model: `hr.payslip.employee.depature.holiday.attests`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `currency_id`, `employee_id`, `fictitious_remuneration_n`, `fictitious_remuneration_n1`, `gross_reference_remuneration_n`, `gross_reference_remuneration_n1`, `leave_allocation_count`, `leave_count`, `leave_type_id`, `net_n`, and 3 more
- Buttons: `compute_termination_holidays`
- XPath or positional patches: 0

## Actions

- `departure_holiday_wizard_action`: `act_window` Departure: Holiday Attests

## Menus

- `menu_l10n_be_hr_payroll_holiday_attests`: Departure: Holiday Attests

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
