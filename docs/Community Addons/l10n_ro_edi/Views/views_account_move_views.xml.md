<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/l10n_ro_edi/l10n_ro_edi|l10n_ro_edi]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_ro_edi_view_account_invoice_filter`
- Name: account.invoice.select.inherit.l10n.ro.edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_ro_edi_state`
- XPath or positional patches: 3

### `in_invoice_tree_inherit_l10n_ro_edi`
- Name: in.invoice.list.inherit.l10n_ro_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_in_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_ro_edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `out_credit_note_tree_inherit_l10n_ro_edi`
- Name: out.credit.note.list.inherit.l10n_ro_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_credit_note_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_ro_edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `out_invoice_tree_inherit_l10n_ro_edi`
- Name: out.invoice.list.inherit.l10n_ro_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_ro_edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `account_move_form_inherit_l10n_ro_edi`
- Name: account.move.form.inherit.l10n_ro_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `datetime`, `key_download`, `l10n_ro_edi_document_ids`, `l10n_ro_edi_index`, `l10n_ro_edi_state`, `state`
- Buttons: `action_l10n_ro_edi_download_attachment`, `action_l10n_ro_edi_fetch_status`
- XPath or positional patches: 2

## Actions

- `l10n_ro_edi_action_fetch_ciusro_status`: `server` Fetch E-Factura Status

## Navigation

- **Parent:** [[docs/Community Addons/l10n_ro_edi/Views]]

<!-- GENERATED:VIEWFILE -->
