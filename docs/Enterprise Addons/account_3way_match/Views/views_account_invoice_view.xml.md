<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_invoice_view.xml

- Module: [[docs/Enterprise Addons/account_3way_match/account_3way_match|account_3way_match]]
- Scope: Enterprise Addons
- Source file: `views/account_invoice_view.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `account_invoice_filter_inherit_account_3way_match`
- Name: account.invoice.select.inherit.account_3way_match
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_bill_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `account_invoice_form_inherit`
- Name: account.move.form.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `force_release_to_pay`, `release_to_pay`, `release_to_pay_manual`
- XPath or positional patches: 1

## Actions

- `account.action_move_in_refund_type`: `act_window`
- `account.action_move_in_invoice_type`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_3way_match/Views]]

<!-- GENERATED:VIEWFILE -->
