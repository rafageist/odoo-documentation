---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_au_payslip_ytd_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_account/l10n_au_hr_payroll_account|l10n_au_hr_payroll_account]]
- Scope: Enterprise Addons
- Source file: `views/l10n_au_payslip_ytd_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_au_payslip_ytd_search`
- Name: l10n_au.payslip.ytd.search
- Model: `l10n_au.payslip.ytd`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `employee_id`
- XPath or positional patches: 0

### `l10n_au_payslip_ytd_list`
- Name: l10n_au.payslip.ytd.list
- Model: `l10n_au.payslip.ytd`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `currency_id`, `employee_id`, `finalised`, `l10n_au_income_stream_type`, `requires_inputs`, `rule_id`, `start_date`, `start_value`, `struct_id`, `ytd_amount`
- Buttons: `%(l10n_au_hr_payroll_account.action_open_transfer_previous_payroll)d`, `action_add_inputs`, `button_finalise`
- XPath or positional patches: 0

### `l10n_au_payslip_ytd_form`
- Name: l10n_au.payslip.ytd.form
- Model: `l10n_au.payslip.ytd`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `employee_id`, `l10n_au_payslip_ytd_input_ids`, `name`, `rule_id`, `struct_id`, `ytd_amount`
- XPath or positional patches: 0

## Actions

- `l10n_au_payslip_ytd_action`: `act_window` YTD Opening Balances

## Menus

- `menu_l10n_au_l10n_au_payslip_ytd`: YTD Opening Balances

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_account/Views]]

