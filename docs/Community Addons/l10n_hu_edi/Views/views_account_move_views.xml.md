<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/l10n_hu_edi/l10n_hu_edi|l10n_hu_edi]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_move_form_inherit_l10n_hu_edi`
- Name: account.move.form.inherit.l10n_hu_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `l10n_hu_edi_attachment`, `l10n_hu_edi_attachment_filename`, `l10n_hu_edi_message_html`, `l10n_hu_edi_messages`, `l10n_hu_edi_send_time`, `l10n_hu_edi_state`, `l10n_hu_edi_transaction_code`, `l10n_hu_invoice_chain_index`, `l10n_hu_payment_mode`
- Buttons: `l10n_hu_edi_button_hide_banner`, `l10n_hu_edi_button_update_status`
- XPath or positional patches: 4

### `view_invoice_tree_inherit_l10n_hu_edi`
- Name: account.invoice.list.inherit.l10n_hu_edi
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_hu_edi_state`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/l10n_hu_edi/Views]]

<!-- GENERATED:VIEWFILE -->
