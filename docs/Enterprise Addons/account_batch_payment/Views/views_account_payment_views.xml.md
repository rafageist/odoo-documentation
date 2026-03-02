<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_payment_views.xml

- Module: [[docs/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]]
- Scope: Enterprise Addons
- Source file: `views/account_payment_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_payment_tree_popup_inherit_account_batch_payment`
- Name: account.payment.list.popup.inherit.account_batch_payment
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `view_account_payment_form_inherit_account_batch_payment`
- Name: account.payment.form.inherit.account_batch_payment
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_form`
- Root tag: `div`
- Field references: 1
- Sample fields: `batch_payment_id`
- Buttons: `button_open_batch_payment`
- XPath or positional patches: 1

### `view_account_payment_tree_inherit_account_batch_payment`
- Name: account.payment.list.inherit.account_batch_payment
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_tree`
- Root tag: `header`
- Field references: 2
- Sample fields: `batch_payment_id`, `partner_id`
- Buttons: `%(action_account_create_batch_payment)d`
- XPath or positional patches: 1

### `view_account_payment_search_inherit_account_batch_payment`
- Name: account.payment.search.inherit.account_batch_payment
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_batch_payment/Views]]

<!-- GENERATED:VIEWFILE -->
