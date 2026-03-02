<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Enterprise Addons/l10n_br_edi/l10n_br_edi|l10n_br_edi]]
- Scope: Enterprise Addons
- Source file: `views/account_move_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_out_invoice_tree_inherit_l10n_br_edi`
- Name: account.move.list.inherit.l10n_br_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_out_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_br_last_edi_status`, `status_in_payment`
- XPath or positional patches: 0

### `account_move_form_inherit_l10n_br_edi`
- Name: account.move.form.inherit.l10n_br_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 14
- Sample fields: `incoterm_location`, `invoice_source_email`, `l10n_br_access_key`, `l10n_br_cfop`, `l10n_br_edi_error`, `l10n_br_edi_freight_model`, `l10n_br_edi_is_needed`, `l10n_br_edi_payment_method`, `l10n_br_edi_transporter_id`, `l10n_br_is_service_transaction`, and 4 more
- Buttons: `action_invoice_sent`, `button_l10n_br_edi_get_service_invoice`, `button_request_cancel`, `button_request_correction`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_br_edi/Views]]

<!-- GENERATED:VIEWFILE -->
