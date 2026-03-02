<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/l10n_es_edi_verifactu/l10n_es_edi_verifactu|l10n_es_edi_verifactu]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_move_form_inherit_l10n_es_edi_verifactu`
- Name: account.move.form.inherit.l10n_es_edi_verifactu
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 11
- Sample fields: `create_date`, `document_type`, `l10n_es_edi_verifactu_available_clave_regimens`, `l10n_es_edi_verifactu_clave_regimen`, `l10n_es_edi_verifactu_document_ids`, `l10n_es_edi_verifactu_refund_reason`, `l10n_es_edi_verifactu_state`, `l10n_es_edi_verifactu_substituted_entry_id`, `l10n_es_edi_verifactu_warning`, `reversed_entry_id`, and 1 more
- Buttons: `l10n_es_edi_verifactu_button_cancel`
- XPath or positional patches: 3

### `view_invoice_tree`
- Name: account.invoice.tree
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_es_edi_verifactu_state`, `status_in_payment`
- XPath or positional patches: 0

### `view_move_tree`
- Name: account.move.tree
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_es_edi_verifactu_state`, `state`
- XPath or positional patches: 0

### `view_account_invoice_filter`
- Name: account.invoice.select
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_account_move_filter`
- Name: account.move.select
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_move_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/l10n_es_edi_verifactu/Views]]

<!-- GENERATED:VIEWFILE -->
