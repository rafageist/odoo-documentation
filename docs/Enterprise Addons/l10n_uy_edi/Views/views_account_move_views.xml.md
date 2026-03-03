---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/l10n_uy_edi/l10n_uy_edi|l10n_uy_edi]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_invoice_filter`
- Name: account.move.view.search
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `search`
- Field references: 2
- Sample fields: `l10n_uy_edi_cfe_state`, `l10n_uy_edi_cfe_uuid`
- XPath or positional patches: 0

### `view_invoice_tree`
- Name: account.move.view.tree
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `list`
- Field references: 1
- Sample fields: `l10n_uy_edi_cfe_state`
- XPath or positional patches: 0

### `view_move_form_inherit_l10n_uy_edi`
- Name: account.move.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `l10n_latam_invoice_document.view_move_form`
- Root tag: `header`
- Field references: 10
- Sample fields: `invoice_incoterm_id`, `l10n_latam_document_number`, `l10n_uy_edi_addenda_ids`, `l10n_uy_edi_cfe_sale_mode`, `l10n_uy_edi_cfe_state`, `l10n_uy_edi_cfe_transport_route`, `l10n_uy_edi_cfe_uuid`, `l10n_uy_edi_document_id`, `l10n_uy_edi_error`, `l10n_uy_edi_journal_type`
- Buttons: `l10n_uy_edi_action_download_preview_xml`, `l10n_uy_edi_action_update_dgi_state`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_uy_edi/Views]]

