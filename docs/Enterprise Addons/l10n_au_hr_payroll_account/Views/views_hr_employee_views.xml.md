---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_account/l10n_au_hr_payroll_account|l10n_au_hr_payroll_account]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_employee_form`
- Name: hr.employee.form.inherit.l10n_au_hr_payroll_account
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `button`
- Field references: 2
- Sample fields: `l10n_au_pay_day`, `l10n_au_report_to_w3`
- Buttons: `%(l10n_au_hr_payroll_account.action_open_payslip_ytd)d`, `action_open_versions`
- XPath or positional patches: 0

### `employee_missing_account_list_view`
- Name: hr.employee.list
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `action_open_payslip_ytd`: `act_window` YTD Balances

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_account/Views]]

