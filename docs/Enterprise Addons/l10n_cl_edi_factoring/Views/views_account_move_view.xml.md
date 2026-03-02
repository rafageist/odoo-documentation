<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Enterprise Addons/l10n_cl_edi_factoring/l10n_cl_edi_factoring|l10n_cl_edi_factoring]]
- Scope: Enterprise Addons
- Source file: `views/account_move_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_invoice_form`
- Name: account.move.aec.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `l10n_cl_edi.view_invoice_form`
- Root tag: `button`
- Field references: 0
- Buttons: `action_l10n_cl_create_aec`, `l10n_cl_verify_dte_status`
- XPath or positional patches: 4

### `account_view_invoice_form`
- Name: account.move.aec.button.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `l10n_cl_button_yield_entry`, `l10n_cl_yield_invoice`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_cl_edi_factoring/Views]]

<!-- GENERATED:VIEWFILE -->
