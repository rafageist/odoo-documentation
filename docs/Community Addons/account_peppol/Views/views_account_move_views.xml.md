<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/account_peppol/account_peppol|account_peppol]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `account_peppol_view_account_invoice_filter`
- Name: account.invoice.select.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `account_peppol_view_out_credit_note_tree_inherit`
- Name: account.move.credit.note.list.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_credit_note_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `peppol_move_state`, `status_in_payment`
- XPath or positional patches: 0

### `account_peppol_view_out_invoice_tree_inherit`
- Name: account.move.out.invoice.list.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `peppol_move_state`, `status_in_payment`
- XPath or positional patches: 0

### `account_peppol_view_move_form`
- Name: account.peppol.view.move.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `header`
- Field references: 0
- Buttons: `action_cancel_peppol_documents`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/account_peppol/Views]]

<!-- GENERATED:VIEWFILE -->
