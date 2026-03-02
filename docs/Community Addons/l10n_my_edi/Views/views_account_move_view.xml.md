<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Community Addons/l10n_my_edi/l10n_my_edi|l10n_my_edi]]
- Scope: Community Addons
- Source file: `views/account_move_view.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_invoice_list_inherit_l10n_my_myinvois`
- Name: account.move.list.inherit.l10n_my_myinvois
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_my_edi_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_move_form_inherit_l10n_my_myinvois`
- Name: account.move.form.inherit.l10n_my_myinvois
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `l10n_my_edi_classification_code`, `l10n_my_edi_custom_form_reference`, `l10n_my_edi_document_ids`, `l10n_my_edi_exemption_reason`, `l10n_my_edi_state`
- Buttons: `action_invoice_sent`, `action_l10n_my_edi_send_invoice`, `action_l10n_my_edi_update_status`, `action_register_payment`, `action_show_myinvois_documents`
- XPath or positional patches: 5

## Actions

- `invoice_send_to_myinvois`: `server` Send To MyInvois

## Navigation

- **Parent:** [[docs/Community Addons/l10n_my_edi/Views]]

<!-- GENERATED:VIEWFILE -->
