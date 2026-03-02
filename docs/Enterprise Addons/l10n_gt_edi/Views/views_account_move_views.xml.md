<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/l10n_gt_edi/l10n_gt_edi|l10n_gt_edi]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_invoice_filter_inherit_l10n_gt_edi`
- Name: account.invoice.select.inherit.l10n_gt_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_gt_edi_state`
- XPath or positional patches: 3

### `view_in_invoice_bill_tree_inherit_l10n_gt_edi`
- Name: account.in.invoice.list.inherit.l10n_gt_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_in_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_gt_edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_out_credit_note_tree_inherit_l10n_gt_edi`
- Name: account.out.credit.note.list.inherit.l10n_gt_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_credit_note_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_gt_edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_out_invoice_tree_inherit_l10n_gt_edi`
- Name: account.out.invoice.list.inherit.l10n_gt_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_gt_edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `account_move_form_inherit_l10n_gt_edi`
- Name: account.move.form.inherit.l10n_gt_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 12
- Sample fields: `datetime`, `l10n_gt_edi_available_doc_types`, `l10n_gt_edi_consignatory_partner`, `l10n_gt_edi_doc_type`, `l10n_gt_edi_document_ids`, `l10n_gt_edi_phrase_ids`, `l10n_gt_edi_state`, `message`, `serial_number`, `series`, and 2 more
- Buttons: `action_download_file`, `l10n_gt_edi_send_bill_to_sat`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_gt_edi/Views]]

<!-- GENERATED:VIEWFILE -->
