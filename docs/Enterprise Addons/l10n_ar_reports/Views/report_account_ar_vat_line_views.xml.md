---
tags: [odoo, enterprise, generated, views]
---

# report/account_ar_vat_line_views.xml

- Module: [[docs/Enterprise Addons/l10n_ar_reports/l10n_ar_reports|l10n_ar_reports]]
- Scope: Enterprise Addons
- Source file: `report/account_ar_vat_line_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_account_ar_vat_line_pivot`
- Name: account.ar.vat.line.pivot
- Model: `account.ar.vat.line`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 19
- Sample fields: `afip_responsibility_type_id`, `base_10`, `base_21`, `base_25`, `base_27`, `base_5`, `city_tax`, `move_type`, `not_taxed`, `other_taxes`, and 9 more
- XPath or positional patches: 0

### `view_account_ar_vat_line_tree`
- Name: account.ar.vat.line.list
- Model: `account.ar.vat.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 20
- Sample fields: `base_10`, `base_21`, `base_25`, `base_27`, `base_5`, `city_tax`, `date`, `move_id`, `not_taxed`, `other_taxes`, and 10 more
- Buttons: `open_journal_entry`
- XPath or positional patches: 0

### `view_account_ar_vat_line_form`
- Name: account.ar.vat.line.form
- Model: `account.ar.vat.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 27
- Sample fields: `afip_responsibility_type_id`, `base_10`, `base_21`, `base_25`, `base_27`, `base_5`, `city_tax`, `company_id`, `date`, `document_type_id`, and 17 more
- XPath or positional patches: 0

### `view_account_ar_vat_line_search`
- Name: account.ar.vat.line.search
- Model: `account.ar.vat.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `afip_responsibility_type_id`, `company_id`, `document_type_id`, `journal_id`, `move_id`, `move_type`, `partner_id`
- XPath or positional patches: 0

## Actions

- `action_account_ar_vat_line`: `act_window` VAT Summary

## Menus

- `menu_current_account`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ar_reports/Views]]

