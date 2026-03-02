<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Enterprise Addons/l10n_mx_edi/l10n_mx_edi|l10n_mx_edi]]
- Scope: Enterprise Addons
- Source file: `views/account_move_view.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_invoice_filter_inherit_l10n_mx_edi`
- Name: view.account.invoice.filter.inherit.l10n_mx_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_invoice_tree_inherit_l10n_mx_edi`
- Name: account.move.list.inherit.l10n_mx_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `l10n_mx_edi_cfdi_sat_state`, `l10n_mx_edi_cfdi_state`, `l10n_mx_edi_cfdi_uuid`, `status_in_payment`
- XPath or positional patches: 0

### `account_move_form_inherit_l10n_mx_edi`
- Name: account.move.form.inherit.l10n_mx_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 27
- Sample fields: `attachment_id`, `attachment_origin`, `attachment_uuid`, `cancel_button_needed`, `cancellation_reason`, `datetime`, `l10n_mx_edi_addenda_ids`, `l10n_mx_edi_cfdi_cancel_id`, `l10n_mx_edi_cfdi_origin`, `l10n_mx_edi_cfdi_sat_state`, and 17 more
- Buttons: `action_cancel`, `action_download_file`, `action_download_payment_receipt`, `action_force_payment_cfdi`, `action_retry`, `action_show_document`, `l10n_mx_edi_cfdi_invoice_try_update_payments`, `l10n_mx_edi_cfdi_try_sat`
- XPath or positional patches: 7

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi/Views]]

<!-- GENERATED:VIEWFILE -->
