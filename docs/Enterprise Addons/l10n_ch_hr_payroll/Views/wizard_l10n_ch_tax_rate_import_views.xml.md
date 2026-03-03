---
tags: [odoo, enterprise, generated, views]
---

# wizard/l10n_ch_tax_rate_import_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `wizard/l10n_ch_tax_rate_import_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_ch_tax_rate_import_wizard_view_form`
- Name: l10n.ch.tax.rate.import.wizard.view.form
- Model: `l10n.ch.tax.rate.import.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `canton`, `canton_mode`, `import_mode`, `tax_file_ids`, `year`
- Buttons: `action_import_file`, `action_import_from_website`
- XPath or positional patches: 0

## Actions

- `l10n_ch_tax_rate_import_wizard_action`: `act_window` Import Tax Rates

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

