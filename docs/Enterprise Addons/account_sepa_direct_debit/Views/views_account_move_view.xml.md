---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Enterprise Addons/account_sepa_direct_debit/account_sepa_direct_debit|account_sepa_direct_debit]]
- Scope: Enterprise Addons
- Source file: `views/account_move_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_move_line_payment_filter`
- Name: sdd.account.move.line.payment.search
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_account_move_line_payment_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_account_invoice_filter`
- Name: sdd.account.invoice.select
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_sepa_direct_debit/Views]]

