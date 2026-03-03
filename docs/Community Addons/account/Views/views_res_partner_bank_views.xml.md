<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_bank_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/res_partner_bank_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_partner_bank_search_inherit`
- Name: res.partner.bank.search.inherit
- Model: `res.partner.bank`
- Type: inferred from arch
- Inherits: `base.view_partner_bank_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_partner_bank_form_inherit_account`
- Name: res.partner.bank.form.inherit.account
- Model: `res.partner.bank`
- Type: inferred from arch
- Inherits: `base.view_partner_bank_form`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `allow_out_payment`, `duplicate_bank_partner_ids`, `has_iban_warning`, `has_money_transfer_warning`, `lock_trust_fields`, `money_transfer_service`, `partner_country_name`, `sanitized_acc_number`, `user_has_group_validate_bank_account`
- XPath or positional patches: 5

## Actions

- `action_account_supplier_accounts`: `act_window` Bank Accounts

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
