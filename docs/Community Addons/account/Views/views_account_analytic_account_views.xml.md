<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_analytic_account_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/account_analytic_account_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `account_analytic_account_view_list_inherit`
- Name: account.analytic.account.list.inherit
- Model: `account.analytic.account`
- Type: inferred from arch
- Inherits: `analytic.view_account_analytic_account_list`
- Root tag: `field`
- Field references: 2
- Sample fields: `credit`, `debit`
- XPath or positional patches: 0

### `account_analytic_account_view_form_inherit`
- Name: account.analytic.account.form.inherit
- Model: `account.analytic.account`
- Type: inferred from arch
- Inherits: `analytic.view_account_analytic_account_form`
- Root tag: `div`
- Field references: 2
- Sample fields: `invoice_count`, `vendor_bill_count`
- Buttons: `action_view_invoice`, `action_view_vendor_bill`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
