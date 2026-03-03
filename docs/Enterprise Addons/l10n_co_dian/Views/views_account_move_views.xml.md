---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/l10n_co_dian/l10n_co_dian|l10n_co_dian]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_invoice_filter_inherit_l10n_co_dian`
- Name: account.invoice.select.inherit.l10n_co_dian
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_co_edi_cufe_cude_ref`, `line_ids`
- XPath or positional patches: 1

### `view_in_invoice_bill_list_inherit_l10n_co_dian`
- Name: account.in.invoice.bill.list.l10n_co_dian
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_in_invoice_bill_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_co_dian_commercial_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_out_invoice_list_inherit_l10n_co_dian`
- Name: account.out.invoice.list.l10n_co_dian
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_co_dian_commercial_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_account_move_form_inherit_l10n_co_dian`
- Name: account.move.form.l10n_co_dian
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 14
- Sample fields: `attachment_id`, `certification_process`, `commercial_state`, `datetime`, `l10n_co_dian_commercial_state`, `l10n_co_dian_document_ids`, `l10n_co_dian_show_support_doc_button`, `l10n_co_edi_cufe_cude_ref`, `message`, `move_id`, and 4 more
- Buttons: `%(action_commercial_event_reject)d`, `action_download_file`, `action_get_attached_document`, `action_get_status`, `l10n_co_dian_action_send_bill_support_document`, `l10n_co_dian_action_update_event_status`, `l10n_co_dian_send_event_update_status_accepted`, `l10n_co_dian_send_event_update_status_accepted_by_issuer`, `l10n_co_dian_send_event_update_status_goods_received`, `l10n_co_dian_send_event_update_status_received`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_co_dian/Views]]

