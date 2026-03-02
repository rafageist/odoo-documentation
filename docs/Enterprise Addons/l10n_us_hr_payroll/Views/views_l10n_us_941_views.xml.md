<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_us_941_views.xml

- Module: [[docs/Enterprise Addons/l10n_us_hr_payroll/l10n_us_hr_payroll|l10n_us_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_us_941_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_us_941_view_list`
- Name: l10n.us.941.view.list
- Model: `l10n.us.941`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `quarter`, `year`
- XPath or positional patches: 0

### `l10n_us_941_view_form`
- Name: l10n.us.941.view.form
- Model: `l10n.us.941`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `company_id`, `csv_file`, `csv_filename`, `date_from`, `date_to`, `employee_id`, `irs_payment_option`, `payslip_ids`, `payslip_run_id`, `quarter`, and 3 more
- Buttons: `action_generate_csv`
- XPath or positional patches: 0

## Actions

- `l10n_us_941_action_view`: `act_window` Form 941

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_us_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
