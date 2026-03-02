<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Community Addons/l10n_ke_edi_tremol/l10n_ke_edi_tremol|l10n_ke_edi_tremol]]
- Scope: Community Addons
- Source file: `views/account_move_view.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_ke_inherit_account_move_search_view`
- Name: l10n.ke.inherit.account.move.search
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_ke_cu_invoice_number`
- XPath or positional patches: 2

### `l10n_ke_inherit_account_move_tree_view`
- Name: l10n.ke.inherit.account.move.list
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_ke_cu_invoice_number`, `status_in_payment`
- XPath or positional patches: 0

### `l10n_ke_inherit_account_move_form`
- Name: l10n.ke.inherit.account.move.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `l10n_ke_cu_datetime`, `l10n_ke_cu_invoice_number`, `l10n_ke_cu_qrcode`, `l10n_ke_cu_serial_number`, `l10n_ke_cu_show_send_button`
- Buttons: `l10n_ke_action_cu_post`
- XPath or positional patches: 3

## Actions

- `action_send_invoices_to_device`: `server` Send to fiscal device

## Navigation

- **Parent:** [[docs/Community Addons/l10n_ke_edi_tremol/Views]]

<!-- GENERATED:VIEWFILE -->
