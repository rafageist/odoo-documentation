---
tags: [odoo, enterprise, generated, views]
---

# wizard/l10n_be_social_balance_sheet_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `wizard/l10n_be_social_balance_sheet_views.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_social_balance_sheet_view_form`
- Name: l10n.be.social.balance.sheet.view.form
- Model: `l10n.be.social.balance.sheet`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `company_id`, `date_from`, `date_to`, `social_balance_filename`, `social_balance_filename_xlsx`, `social_balance_sheet`, `social_balance_xlsx`, `state`, `state_xlsx`
- Buttons: `export_report_xlsx`, `print_report`
- XPath or positional patches: 0

## Actions

- `l10n_be_social_balance_sheet_action`: `act_window` Social Balance Sheet

## Menus

- `menu_l10n_be_social_balance_sheet`: Social Balance Sheet

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

