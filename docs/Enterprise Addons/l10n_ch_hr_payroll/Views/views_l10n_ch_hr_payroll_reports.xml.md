<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_hr_payroll_reports.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_hr_payroll_reports.xml`
- Views: 2
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `view_l10n_ch_master_data_report_wizard_tree`
- Name: l10n.ch.master.data.report.tree
- Model: `l10n.ch.master.data.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `month`, `year`
- XPath or positional patches: 0

### `view_l10n_ch_master_data_report_wizard_form`
- Name: l10n.ch.master.data.report.form
- Model: `l10n.ch.master.data.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `company_id`, `master_report_pdf_file`, `master_report_pdf_filename`, `month`, `wage_type_pdf_file`, `wage_type_pdf_filename`, `year`
- Buttons: `action_generate_pdf`
- XPath or positional patches: 0

## Actions

- `action_l10n_ch_company_wage_type_report`: `report` Company Wage Type Report
- `action_l10n_ch_company_master_data_report`: `report` Company Master Data Report
- `action_l10n_ch_master_data_report_wizard`: `act_window` Swiss Master Data Report

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
