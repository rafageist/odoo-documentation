<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_payment_view.xml

- Module: [[docs/Enterprise Addons/account_sepa_direct_debit/account_sepa_direct_debit|account_sepa_direct_debit]]
- Scope: Enterprise Addons
- Source file: `views/account_payment_view.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_payment_search`
- Name: sdd.account.payment.search
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_account_payment_tree`
- Name: sdd.account.payment.list
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `sdd_mandate_id`, `sdd_mandate_scheme`
- XPath or positional patches: 2

### `sdd_view_account_payment_search`
- Name: sdd.account.account.payment.search
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `sdd_account_payment_form`
- Name: sdd.account.payment.form
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sdd_mandate_id`
- XPath or positional patches: 2

### `sdd_account_payment_with_mandates_tree`
- Name: sdd.account.payment.mandate.list
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_tree`
- Root tag: `list`
- Field references: 1
- Sample fields: `sdd_mandate_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_sepa_direct_debit/Views]]

<!-- GENERATED:VIEWFILE -->
