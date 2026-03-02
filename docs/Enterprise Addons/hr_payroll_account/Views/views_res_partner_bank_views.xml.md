<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/res_partner_bank_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll_account/hr_payroll_account|hr_payroll_account]]
- Scope: Enterprise Addons
- Source file: `views/res_partner_bank_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_partner_bank_tree_inherit`
- Name: res.partner.bank.list.inherit
- Model: `res.partner.bank`
- Type: inferred from arch
- Inherits: `base.view_partner_bank_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `bank_bic`
- XPath or positional patches: 1

### `view_partner_bank_form_inherit_hr_payroll_account`
- Name: res.partner.bank.form.inherit.hr.payroll.account
- Model: `res.partner.bank`
- Type: inferred from arch
- Inherits: `account.view_partner_bank_form_inherit_account`
- Root tag: `field`
- Field references: 1
- Sample fields: `partner_id`
- XPath or positional patches: 0

### `view_partner_bank_search_inherit`
- Name: res.partner.bank.search.inherit
- Model: `res.partner.bank`
- Type: inferred from arch
- Inherits: `base.view_partner_bank_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `action_res_partner_bank_account_form`: `act_window` Bank Accounts

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll_account/Views]]

<!-- GENERATED:VIEWFILE -->
