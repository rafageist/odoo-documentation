<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/l10n_jo_edi/l10n_jo_edi|l10n_jo_edi]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_invoice_filter`
- Name: account.invoice.select
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_out_credit_note_tree`
- Name: account.move.tree
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_credit_note_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `l10n_jo_edi_error`, `l10n_jo_edi_invoice_type`, `l10n_jo_edi_state`, `payment_reference`
- XPath or positional patches: 0

### `view_out_invoice_tree`
- Name: account.move.tree
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_invoice_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `l10n_jo_edi_error`, `l10n_jo_edi_invoice_type`, `l10n_jo_edi_state`, `payment_reference`
- XPath or positional patches: 0

### `view_move_form`
- Name: account.move.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `l10n_jo_edi_error`, `l10n_jo_edi_invoice_type`, `l10n_jo_edi_is_needed`, `l10n_jo_edi_qr`, `l10n_jo_edi_state`, `reversed_entry_id`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Community Addons/l10n_jo_edi/Views]]

<!-- GENERATED:VIEWFILE -->
