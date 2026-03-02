<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/report_hr_esic_views.xml

- Module: [[docs/Enterprise Addons/l10n_in_hr_payroll/l10n_in_hr_payroll|l10n_in_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/report_hr_esic_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `hr_esic_report_view_form`
- Name: unnamed
- Model: `l10n.in.hr.payroll.esic.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `export_report_type`, `month`, `xlsx_file`, `xlsx_filename`, `year`
- Buttons: `action_export_xlsx`
- XPath or positional patches: 0

### `hr_esic_report_view_list`
- Name: unnamed
- Model: `l10n.in.hr.payroll.esic.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `export_report_type`, `month`, `year`
- XPath or positional patches: 0

## Actions

- `l10n_in_hr_esic_report_action`: `act_window` ESI Report

## Menus

- `l10n_in_hr_esic_report_menu`: ESI Report

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_in_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
