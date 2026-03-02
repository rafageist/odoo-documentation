<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_monthly_summary_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_monthly_summary_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_ch_monthly_summary_view_tree`
- Name: l10n.ch.monthly.summary.view.list
- Model: `l10n.ch.monthly.summary`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `date_end`, `date_start`, `month`, `year`
- XPath or positional patches: 0

### `l10n_ch_monthly_summary_view_form`
- Name: l10n.ch.monthly.summary.view.form
- Model: `l10n.ch.monthly.summary`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `aggregation_type`, `company_ids`, `currency_id`, `date_end`, `date_start`, `month`, `monthly_summary_pdf_file`, `monthly_summary_pdf_filename`, `monthly_summary_xls_file`, `monthly_summary_xls_filename`, and 1 more
- Buttons: `action_generate_pdf`, `action_generate_xls`
- XPath or positional patches: 0

## Actions

- `l10n_ch_monthly_summary_action`: `act_window` Monthly Summary

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
