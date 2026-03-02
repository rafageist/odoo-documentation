<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move.xml

- Module: [[docs/Community Addons/l10n_id_efaktur_coretax/l10n_id_efaktur_coretax|l10n_id_efaktur_coretax]]
- Scope: Community Addons
- Source file: `views/account_move.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_account_invoice_filter`
- Name: account.move.select.l10n_id.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_id_coretax_document`, `name`
- XPath or positional patches: 0

### `account_move_efaktur_form_view`
- Name: account.move.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `l10n_id_coretax_add_info_07`, `l10n_id_coretax_add_info_08`, `l10n_id_coretax_custom_doc`, `l10n_id_coretax_custom_doc_month_year`, `l10n_id_coretax_document`, `l10n_id_coretax_efaktur_available`, `l10n_id_coretax_facility_info_07`, `l10n_id_coretax_facility_info_08`, `l10n_id_kode_transaksi`
- XPath or positional patches: 1

## Actions

- `dowload_efaktur_action`: `server` Download e-Faktur

## Navigation

- **Parent:** [[docs/Community Addons/l10n_id_efaktur_coretax/Views]]

<!-- GENERATED:VIEWFILE -->
