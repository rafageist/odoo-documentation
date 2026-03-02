<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/l10n_tr_nilvera_einvoice/l10n_tr_nilvera_einvoice|l10n_tr_nilvera_einvoice]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `account_nilvera_view_invoice_tree`
- Name: account.nilvera.invoice.list
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_tr_nilvera_send_status`
- XPath or positional patches: 1

### `account_nilvera_view_account_invoice_filter`
- Name: account.nilvera.invoice.select
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `account_nilvera_view_move_form`
- Name: account.nilvera.view.move.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_tr_nilvera_send_status`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/l10n_tr_nilvera_einvoice/Views]]

<!-- GENERATED:VIEWFILE -->
