<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/views.xml

- Module: [[docs/Enterprise Addons/l10n_uk_reports/l10n_uk_reports|l10n_uk_reports]]
- Scope: Enterprise Addons
- Source file: `views/views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `hmrc_vat_obligation_form`
- Name: HMRC MTD VAT Obigations
- Model: `l10n_uk.vat.obligation`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `company_id`, `date_due`, `date_end`, `date_received`, `date_start`, `status`
- XPath or positional patches: 0

### `hmrc_vat_obligation_tree`
- Name: HMRC MTD VAT Obigations
- Model: `l10n_uk.vat.obligation`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `date_due`, `date_end`, `date_received`, `date_start`, `status`
- XPath or positional patches: 0

## Actions

- `action_hmrc_vat_obligation_view_menu`: `act_window` HMRC VAT Obligations

## Menus

- `menu_hmrc_vat_obligation`: VAT Obligations

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_uk_reports/Views]]

<!-- GENERATED:VIEWFILE -->
