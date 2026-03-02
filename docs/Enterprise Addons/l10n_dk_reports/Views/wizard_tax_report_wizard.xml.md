<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# wizard/tax_report_wizard.xml

- Module: [[docs/Enterprise Addons/l10n_dk_reports/l10n_dk_reports|l10n_dk_reports]]
- Scope: Enterprise Addons
- Source file: `wizard/tax_report_wizard.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_dk_reports_rsu_tax_report_receipt_wizard_form`
- Name: l10n_dk_reports.tax.report.receipt.wizard.view.form
- Model: `l10n_dk_reports.tax.report.receipt.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `deadline_date`, `ocr_account_number`, `ocr_card_type_code`, `ocr_identification_number`, `payment_ref`
- Buttons: `action_approve_tax_report`, `action_download_pdf`, `action_receive_receipt`
- XPath or positional patches: 0

### `l10n_dk_reports_rsu_tax_report_submit_draft_wizard_form`
- Name: l10n_dk_reports.tax.report.submit.draft.wizard.view.form
- Model: `l10n_dk_reports.tax.report.submit.draft.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `deadline_date`, `due_date`, `end_date`, `frequency_code`, `payment_date`, `settlement_period_end`, `settlement_period_start`, `start_date`
- Buttons: `action_submit_draft`
- XPath or positional patches: 0

### `l10n_dk_reports_rsu_tax_report_calendar_wizard_form`
- Name: l10n_dk_reports.tax.report.calendar.wizard.view.form
- Model: `l10n_dk_reports.tax.report.calendar.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `date_from`, `date_to`, `description`
- Buttons: `action_call_company_calendar`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_dk_reports/Views]]

<!-- GENERATED:VIEWFILE -->
