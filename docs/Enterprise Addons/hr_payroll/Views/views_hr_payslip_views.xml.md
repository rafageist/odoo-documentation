<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_views.xml`
- Views: 5
- Actions: 9
- Menus: 0
- Rules: 0

## View records

### `view_hr_payslip_filter`
- Name: hr.payslip.select
- Model: `hr.payslip`
- Type: inferred from arch
- Root tag: `search`
- Field references: 8
- Sample fields: `activity_type_id`, `activity_user_id`, `date_from`, `employee_id`, `name`, `payslip_run_id`, `struct_id`, `version_id`
- XPath or positional patches: 0

### `view_hr_payslip_pivot`
- Name: hr.payslip.pivot
- Model: `hr.payslip`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `department_id`, `net_wage`
- XPath or positional patches: 0

### `view_hr_payslip_form`
- Name: hr.payslip.form
- Model: `hr.payslip`
- Type: inferred from arch
- Root tag: `form`
- Field references: 50
- Sample fields: `_allowed_input_type_ids`, `amount`, `category_id`, `code`, `company_id`, `country_code`, `country_id`, `credit_note`, `currency_id`, `date_from`, and 40 more
- Buttons: `action_adjust_payslip`, `action_configure_payslip_inputs`, `action_export_payslip`, `action_keep_wrong_version`, `action_open_related_payslips`, `action_open_salary_attachments`, `action_open_work_entries`, `action_payslip_cancel`, `action_payslip_done`, `action_payslip_draft`, and 7 more
- XPath or positional patches: 0

### `hr_payslip_view_kanban`
- Name: hr.payslip.kanban
- Model: `hr.payslip`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `currency_id`, `date_from`, `date_to`, `employee_id`, `name`, `net_wage`, `state`
- XPath or positional patches: 0

### `view_hr_payslip_tree`
- Name: hr.payslip.list
- Model: `hr.payslip`
- Type: inferred from arch
- Root tag: `list`
- Field references: 14
- Sample fields: `basic_wage`, `company_id`, `currency_id`, `date_from`, `date_to`, `employee_id`, `employee_reference`, `employer_cost`, `gross_wage`, `issues`, and 4 more
- Buttons: `action_move_to_off_cycle`, `action_payslip_done`, `action_payslip_paid`, `action_print_payslip`, `action_validate`, `compute_sheet`
- XPath or positional patches: 0

## Actions

- `action_hr_payroll_remove_from_payrun`: `server` Send to Off-Cycle
- `action_hr_payroll_recompute_whole_sheet`: `server` Recompute Whole Sheet
- `action_hr_payroll_cancel_payroll`: `server` Cancel
- `action_hr_payroll_confirm_payroll`: `server` Confirm
- `action_hr_payroll_compute_payroll`: `server` Compute Sheet
- `action_hr_payroll_draft`: `server` Set to Draft
- `act_hr_employee_payslip_list`: `act_window` Payslips
- `action_view_hr_payslip_month_form`: `act_window` Employee Payslips
- `action_hr_payslip_new`: `act_window` Employee Payslips

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
