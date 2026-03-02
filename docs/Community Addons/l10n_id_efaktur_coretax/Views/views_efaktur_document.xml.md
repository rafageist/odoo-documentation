<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/efaktur_document.xml

- Module: [[docs/Community Addons/l10n_id_efaktur_coretax/l10n_id_efaktur_coretax|l10n_id_efaktur_coretax]]
- Scope: Community Addons
- Source file: `views/efaktur_document.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_id_efaktur_document_filter_view`
- Name: l10n_id.efaktur_coretax.document.filter.view
- Model: `l10n_id_efaktur_coretax.document`
- Type: inferred from arch
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 0

### `l10n_id_efaktur_document_list_view`
- Name: l10n_id.efaktur_coretax.document.list.view
- Model: `l10n_id_efaktur_coretax.document`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `invoice_ids`, `name`
- XPath or positional patches: 0

### `l10n_id_efaktur_document_form_view`
- Name: l10n_id.efaktur_coretax.document.form.view
- Model: `l10n_id_efaktur_coretax.document`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `amount_tax_signed`, `amount_total_in_currency_signed`, `amount_untaxed_in_currency_signed`, `attachment_id`, `company_id`, `currency_id`, `invoice_date`, `invoice_ids`, `name`, `status_in_payment`
- Buttons: `action_download`, `action_regenerate`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/l10n_id_efaktur_coretax/Views]]

<!-- GENERATED:VIEWFILE -->
