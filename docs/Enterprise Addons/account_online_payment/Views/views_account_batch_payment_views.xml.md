<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_batch_payment_views.xml

- Module: [[docs/Enterprise Addons/account_online_payment/account_online_payment|account_online_payment]]
- Scope: Enterprise Addons
- Source file: `views/account_batch_payment_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_batch_payment_tree_inherit`
- Name: sct.account.batch.payment.tree.inherit
- Model: `account.batch.payment`
- Type: inferred from arch
- Inherits: `account_batch_payment.view_batch_payment_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `payment_online_status`
- XPath or positional patches: 1

### `view_batch_payment_form_inherit`
- Name: sct.account.batch.payment.form.inherit
- Model: `account.batch.payment`
- Type: inferred from arch
- Inherits: `account_batch_payment.view_batch_payment_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `payment_online_status`
- Buttons: `export_batch_payment`, `initiate_payment`, `validate_batch_button`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_online_payment/Views]]

<!-- GENERATED:VIEWFILE -->
