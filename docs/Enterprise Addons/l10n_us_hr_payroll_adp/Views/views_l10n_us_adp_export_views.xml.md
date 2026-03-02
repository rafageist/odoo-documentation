<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_us_adp_export_views.xml

- Module: [[docs/Enterprise Addons/l10n_us_hr_payroll_adp/l10n_us_hr_payroll_adp|l10n_us_hr_payroll_adp]]
- Scope: Enterprise Addons
- Source file: `views/l10n_us_adp_export_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_us_adp_export_view_tree`
- Name: l10n.us.adp.export.view.list
- Model: `l10n.us.adp.export`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `batch_id`, `end_date`, `start_date`
- XPath or positional patches: 0

### `l10n_us_adp_export_view_form`
- Name: l10n.us.adp.export.view.form
- Model: `l10n.us.adp.export`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `batch_description`, `batch_id`, `company_id`, `csv_file`, `csv_filename`, `department_id`, `employee_ids`, `end_date`, `l10n_us_adp_code`, `name`, and 3 more
- Buttons: `action_generate_csv`, `action_open_work_entries`
- XPath or positional patches: 0

## Actions

- `l10n_us_adp_export_action`: `act_window` Export to ADP

## Menus

- `menu_l10n_us_adp_export`: ADP Export

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_us_hr_payroll_adp/Views]]

<!-- GENERATED:VIEWFILE -->
