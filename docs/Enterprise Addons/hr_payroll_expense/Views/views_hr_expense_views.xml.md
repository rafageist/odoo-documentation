<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_expense_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll_expense/hr_payroll_expense|hr_payroll_expense]]
- Scope: Enterprise Addons
- Source file: `views/hr_expense_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_expense_view_form_inherit_payroll`
- Name: hr.expense.view.form.payroll
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense.hr_expense_view_form`
- Root tag: `div`
- Field references: 2
- Sample fields: `payslip_id`, `refund_in_payslip`
- Buttons: `action_open_payslip`, `action_remove_from_payslip`, `action_report_in_next_payslip`
- XPath or positional patches: 8

## Actions

- `hr_expense_add_to_payslip_action_server`: `server` Report in Next Payslip

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll_expense/Views]]

<!-- GENERATED:VIEWFILE -->
