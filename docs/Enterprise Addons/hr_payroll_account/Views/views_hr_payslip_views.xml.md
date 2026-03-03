---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll_account/hr_payroll_account|hr_payroll_account]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_payslip_view_form`
- Name: hr.payslip.inherit.form
- Model: `hr.payslip`
- Type: inferred from arch
- Inherits: `hr_payroll.view_hr_payslip_form`
- Root tag: `div`
- Field references: 5
- Sample fields: `batch_payroll_move_lines`, `date`, `journal_id`, `move_id`, `paid`
- Buttons: `action_open_move`, `action_payslip_done`, `action_payslip_paid`, `action_register_payment`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll_account/Views]]

