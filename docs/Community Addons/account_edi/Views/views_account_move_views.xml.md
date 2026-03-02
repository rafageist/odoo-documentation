<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/account_edi/account_edi|account_edi]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 6
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_move_form_inherit`
- Name: account.move.form.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 14
- Sample fields: `blocking_level`, `edi_blocking_level`, `edi_document_ids`, `edi_error_count`, `edi_error_message`, `edi_format_name`, `edi_show_abandon_cancel_button`, `edi_show_cancel_button`, `edi_show_force_cancel_button`, `edi_state`, and 4 more
- Buttons: `%(account_edi.action_open_edi_documents)d`, `action_export_xml`, `action_retry_edi_documents_error`, `button_abandon_cancel_posted_posted_moves`, `button_cancel_posted_moves`, `button_force_cancel`, `button_process_edi_web_services`
- XPath or positional patches: 4

### `view_account_invoice_filter`
- Name: account.invoice.select.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_in_bill_tree_inherit`
- Name: account.move.tree.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_in_invoice_bill_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `edi_blocking_level`, `edi_error_message`, `edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_in_invoice_refund_tree_inherit`
- Name: account.move.list.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_in_invoice_refund_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `edi_blocking_level`, `edi_error_message`, `edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_out_credit_note_tree_inherit`
- Name: account.move.list.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_credit_note_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `edi_blocking_level`, `edi_error_message`, `edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_out_invoice_tree_inherit`
- Name: account.move.list.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_invoice_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `edi_blocking_level`, `edi_error_message`, `edi_state`, `status_in_payment`
- XPath or positional patches: 0

## Actions

- `account_edi.action_open_edi_documents`: `act_window` Electronic invoicing

## Navigation

- **Parent:** [[docs/Community Addons/account_edi/Views]]

<!-- GENERATED:VIEWFILE -->
