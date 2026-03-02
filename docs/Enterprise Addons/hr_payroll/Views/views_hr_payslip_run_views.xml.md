<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_run_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_run_views.xml`
- Views: 6
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `hr_payslip_run_form`
- Name: hr.payslip.run.form
- Model: `hr.payslip.run`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `company_id`, `date_end`, `date_start`, `schedule_pay`, `structure_id`
- XPath or positional patches: 0

### `hr_payslip_run_view_graph`
- Name: hr.payslip.run.graph
- Model: `hr.payslip.run`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 0
- XPath or positional patches: 0

### `hr_payslip_run_view_pivot`
- Name: hr.payslip.run.pivot
- Model: `hr.payslip.run`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 0
- XPath or positional patches: 0

### `hr_payslip_run_view_calendar`
- Name: hr.payslip.run.calendar
- Model: `hr.payslip.run`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 1
- Sample fields: `state`
- XPath or positional patches: 0

### `hr_payslip_run_view_kanban`
- Name: hr.payslip.run.kanban
- Model: `hr.payslip.run`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 15
- Sample fields: `color`, `currency_id`, `date_end`, `date_start`, `gross_sum`, `has_error`, `name`, `net_sum`, `payment_report`, `payment_report_filename`, and 5 more
- Buttons: `action_confirm`, `action_draft`, `action_paid`, `action_payment_report`, `action_payroll_hr_version_list_view_payrun`, `action_unpaid`, `action_validate`, `unlink`
- XPath or positional patches: 0

### `hr_payslip_run_filter`
- Name: hr.payslip.run.search
- Model: `hr.payslip.run`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `action_hr_payroll_open_pay_run`: `act_window` Pay Run Payslips
- `action_hr_payslip_run`: `act_window` Pay Runs
- `action_hr_payslip_run_create`: `act_window` New Pay Run

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
