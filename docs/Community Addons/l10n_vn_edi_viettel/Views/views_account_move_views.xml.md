---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/l10n_vn_edi_viettel/l10n_vn_edi_viettel|l10n_vn_edi_viettel]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_invoice_tree_inherit_l10n_vn_edi`
- Name: account.invoice.list.inherit.l10n_vn_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_vn_edi_invoice_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_account_invoice_filter_inherit_l10n_vn_edi`
- Name: account.invoice.select.inherit.l10n_vn_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `filter`
- Field references: 1
- Sample fields: `l10n_vn_edi_invoice_state`
- XPath or positional patches: 1

### `view_invoice_form_inherit_l10n_vn_edi`
- Name: account.move.form.inherit.l10n_vn_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `l10n_vn_edi_adjustment_type`, `l10n_vn_edi_agreement_document_date`, `l10n_vn_edi_agreement_document_name`, `l10n_vn_edi_invoice_number`, `l10n_vn_edi_invoice_state`, `l10n_vn_edi_invoice_symbol`, `l10n_vn_edi_issue_date`, `l10n_vn_edi_reservation_code`
- Buttons: `action_l10n_vn_edi_update_payment_status`
- XPath or positional patches: 2

## Actions

- `l10n_vn_edi_send_invoice_payment_status`: `server` Send payment status to SInvoice

## Navigation

- **Parent:** [[docs/Community Addons/l10n_vn_edi_viettel/Views]]

