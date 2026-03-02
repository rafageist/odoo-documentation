<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/l10n_in_reports/l10n_in_reports|l10n_in_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_invoice_filter`
- Name: account.invoice.select.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_account_move_form_inherit_account`
- Name: account.move.form.inherit.account
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `l10n_in_exception`, `l10n_in_gstr2b_reconciliation_status`, `l10n_in_irn_number`
- Buttons: `action_l10n_in_bill_reset_gstr2b_manual_matching`, `action_l10n_in_bill_set_gstr2b_manual_matching`, `l10n_in_update_move_using_irn`
- XPath or positional patches: 5

### `view_move_line_form_l10n_in`
- Name: account.move.line.form.l10n_in
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_in_hsn_code`
- XPath or positional patches: 1

### `view_move_line_tree_l10n_in`
- Name: account.move.line.list.l10n_in
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_in_hsn_code`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_in_reports/Views]]

<!-- GENERATED:VIEWFILE -->
