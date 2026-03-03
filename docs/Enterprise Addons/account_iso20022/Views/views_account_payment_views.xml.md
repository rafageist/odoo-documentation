---
tags: [odoo, enterprise, generated, views]
---

# views/account_payment_views.xml

- Module: [[docs/Enterprise Addons/account_iso20022/account_iso20022|account_iso20022]]
- Scope: Enterprise Addons
- Source file: `views/account_payment_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_batch_payment_form_inherit_account_iso20022`
- Name: account.payment.form.inherit.account_iso20022
- Model: `account.batch.payment`
- Type: inferred from arch
- Inherits: `account_batch_payment.view_batch_payment_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `amount_signed`, `iso20022_priority`
- XPath or positional patches: 0

### `view_account_payment_tree_inherit_account_sepa_pain_09`
- Name: account.payment.list.inherit.account_sepa_pain_09
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `iso20022_priority`, `iso20022_uetr`, `state`
- XPath or positional patches: 0

### `view_account_payment_form_inherit_account_sepa_pain_09`
- Name: account.payment.form.inherit.account_sepa_pain_09
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `end_to_end_uuid`, `iso20022_charge_bearer`, `iso20022_priority`, `iso20022_uetr`
- XPath or positional patches: 2

### `view_account_payment_search_inherit_account_sepa_pain_09`
- Name: account.payment.search.inherit.account_sepa_pain_09
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `iso20022_uetr`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_iso20022/Views]]

