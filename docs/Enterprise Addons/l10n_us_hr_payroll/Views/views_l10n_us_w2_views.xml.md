<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_us_w2_views.xml

- Module: [[docs/Enterprise Addons/l10n_us_hr_payroll/l10n_us_hr_payroll|l10n_us_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_us_w2_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_us_w2_view_tree`
- Name: l10n.us.w2.view.list
- Model: `l10n.us.w2`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `date_end`, `date_start`
- XPath or positional patches: 0

### `l10n_us_w2_view_form`
- Name: l10n.us.w2.view.form
- Model: `l10n.us.w2`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `allowed_payslip_ids`, `company_id`, `csv_file`, `csv_filename`, `date_end`, `date_from`, `date_start`, `date_to`, `employee_id`, `payslip_ids`, and 2 more
- Buttons: `action_generate_csv`
- XPath or positional patches: 0

## Actions

- `l10n_us_w2_action`: `act_window` Create W2 Form

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_us_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
