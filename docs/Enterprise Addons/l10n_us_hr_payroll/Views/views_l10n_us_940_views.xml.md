---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_us_940_views.xml

- Module: [[docs/Enterprise Addons/l10n_us_hr_payroll/l10n_us_hr_payroll|l10n_us_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_us_940_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_us_940_view_list`
- Name: l10n.us.940.view.list
- Model: `l10n.us.940`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `year`
- XPath or positional patches: 0

### `l10n_us_940_view_form`
- Name: l10n.us.940.view.form
- Model: `l10n.us.940`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `company_id`, `csv_file`, `csv_filename`, `date_from`, `date_to`, `employee_id`, `has_paid_credit_reduction_state`, `irs_payment_option`, `is_multi_state_employer`, `payslip_ids`, and 4 more
- Buttons: `action_generate_csv`
- XPath or positional patches: 0

## Actions

- `l10n_us_940_action_view`: `act_window` Form 940

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_us_hr_payroll/Views]]

