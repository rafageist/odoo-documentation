<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_au_stp_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_account/l10n_au_hr_payroll_account|l10n_au_hr_payroll_account]]
- Scope: Enterprise Addons
- Source file: `views/l10n_au_stp_views.xml`
- Views: 4
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `l10n_au_stp_emp_view_form`
- Name: l10n_au.stp.emp.form
- Model: `l10n_au.stp.emp`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `currency_id`, `employee_id`, `payslip_ids`, `ytd_balance_ids`, `ytd_gross`, `ytd_rfba`, `ytd_rfbae`, `ytd_super`, `ytd_tax`
- XPath or positional patches: 0

### `l10n_au_stp_view_search`
- Name: l10n_au.stp.view.search
- Model: `l10n_au.stp`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `payslip_batch_id`, `payslip_ids`
- XPath or positional patches: 0

### `l10n_au_stp_view_tree`
- Name: l10n_au.stp.list
- Model: `l10n_au.stp`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `activity_date_deadline`, `activity_ids`, `file_replacement_message`, `name`, `payevent_type`, `payslip_batch_id`, `state`
- XPath or positional patches: 0

### `l10n_au_stp_form_wizard`
- Name: l10n_au.stp.form
- Model: `l10n_au.stp`
- Type: inferred from arch
- Root tag: `form`
- Field references: 27
- Sample fields: `company_id`, `currency_id`, `date_from`, `date_to`, `employee_id`, `end_date`, `ffr`, `file_replacement_message`, `is_zeroing`, `l10n_au_stp_emp`, and 17 more
- Buttons: `action_replace_file`, `l10n_au_hr_payroll_account.l10n_au_action_submit_stp`
- XPath or positional patches: 0

## Actions

- `l10n_au_stp_action`: `act_window` Single Touch Payroll
- `l10n_au_action_submit_stp`: `act_window` Submit to ATO

## Menus

- `menu_l10n_au_l10n_au_stp`: Single Touch Payroll

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_account/Views]]

<!-- GENERATED:VIEWFILE -->
