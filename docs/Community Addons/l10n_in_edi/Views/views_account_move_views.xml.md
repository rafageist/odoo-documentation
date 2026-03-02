<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/l10n_in_edi/l10n_in_edi|l10n_in_edi]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_in_edi_inherit_account_move_search_view`
- Name: l10n.in.edi.inherit.account.move.search
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `view_out_credit_note_tree_inherit_l10n_in_edi`
- Name: out.credit.note.list.inherit.l10n_in_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_credit_note_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_in_edi_status`, `status_in_payment`
- XPath or positional patches: 0

### `view_out_invoice_tree_inherit_l10n_in_edi`
- Name: out.invoice.list.inherit.l10n_in_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_in_edi_status`, `status_in_payment`
- XPath or positional patches: 0

### `invoice_form_inherit_l10n_in_edi`
- Name: account.move.form.inherit.l10n.in.edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `l10n_in_edi_cancel_reason`, `l10n_in_edi_cancel_remarks`, `l10n_in_edi_error`, `l10n_in_edi_status`
- Buttons: `action_export_l10n_in_edi_content_json`, `action_l10n_in_edi_force_cancel`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Community Addons/l10n_in_edi/Views]]

<!-- GENERATED:VIEWFILE -->
