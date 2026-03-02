<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/l10n_gr_edi/l10n_gr_edi|l10n_gr_edi]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_account_invoice_filter_inherit_l10n_gr_edi`
- Name: account.invoice.select.inherit.l10n_gr_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_gr_edi_state`
- XPath or positional patches: 3

### `view_in_invoice_bill_tree_inherit_l10n_gr_edi`
- Name: account.in.invoice.list.inherit.l10n_gr_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_in_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_gr_edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_out_credit_note_tree_inherit_l10n_gr_edi`
- Name: account.out.credit.note.list.inherit.l10n_gr_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_credit_note_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_gr_edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_out_invoice_tree_inherit_l10n_gr_edi`
- Name: account.out.invoice.list.inherit.l10n_gr_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_gr_edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `account_move_form_inherit_l10n_gr_edi`
- Name: account.move.form.inherit.l10n_gr_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `header`
- Field references: 22
- Sample fields: `attachment_id`, `datetime`, `l10n_gr_edi_alerts`, `l10n_gr_edi_available_cls_category`, `l10n_gr_edi_available_cls_type`, `l10n_gr_edi_available_cls_vat`, `l10n_gr_edi_available_inv_type`, `l10n_gr_edi_cls_category`, `l10n_gr_edi_cls_mark`, `l10n_gr_edi_cls_type`, and 12 more
- Buttons: `action_download`, `l10n_gr_edi_try_send_expense_classification`
- XPath or positional patches: 6

## Actions

- `l10n_gr_edi_action_try_send_batch`: `server` Send to myDATA

## Navigation

- **Parent:** [[docs/Community Addons/l10n_gr_edi/Views]]

<!-- GENERATED:VIEWFILE -->
