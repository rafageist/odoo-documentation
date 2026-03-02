<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# wizard/hr_payroll_allocating_paid_time_off_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `wizard/hr_payroll_allocating_paid_time_off_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_hr_payroll_alloc_employee_view_tree`
- Name: hr.payroll.alloc.employee.view.list
- Model: `hr.payroll.alloc.employee`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `contract_next_year_id`, `employee_id`, `paid_time_off`, `paid_time_off_to_allocate`, `resource_calendar_id`
- XPath or positional patches: 0

### `hr_payroll_allocating_paid_time_off_view_form`
- Name: hr.payroll.alloc.paid.leave.view.form
- Model: `hr.payroll.alloc.paid.leave`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `alloc_employee_ids`, `company_id`, `department_id`, `holiday_status_id`, `structure_type_id`, `year`
- Buttons: `generate_allocation`
- XPath or positional patches: 0

## Actions

- `allocating_paid_time_off_wizard_action`: `act_window` Paid Time Off Allocation

## Menus

- `menu_hr_allocating_paid_time_off_view`: Paid Time Off Allocation

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
