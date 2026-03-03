---
tags: [odoo, enterprise, generated, views]
---

# views/sdd_mandate_views.xml

- Module: [[docs/Enterprise Addons/account_sepa_direct_debit/account_sepa_direct_debit|account_sepa_direct_debit]]
- Scope: Enterprise Addons
- Source file: `views/sdd_mandate_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `account_sdd_mandate_search_view`
- Name: sdd.mandate.search
- Model: `sdd.mandate`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `name`, `partner_bank_id`, `partner_id`
- XPath or positional patches: 0

### `account_sepa_direct_debit_mandate_tree`
- Name: sdd.mandate.list
- Model: `sdd.mandate`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `company_id`, `end_date`, `name`, `partner_id`, `pre_notification_period`, `sdd_scheme`, `start_date`, `state`
- XPath or positional patches: 0

### `view_partner_bank_form_inherit_account_sepa_direct_debit`
- Name: res.partner.bank.view.form.inherit.account.sepa.direct.debit
- Model: `res.partner.bank`
- Type: inferred from arch
- Inherits: `base.view_partner_bank_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `partner_id`
- XPath or positional patches: 0

### `account_sepa_direct_debit_mandate_form`
- Name: sdd.mandate.form
- Model: `sdd.mandate`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `company_id`, `end_date`, `name`, `paid_invoices_nber`, `partner_bank_id`, `partner_id`, `partner_parent_id`, `payments_to_collect_nber`, `pre_notification_period`, `sdd_scheme`, and 2 more
- Buttons: `action_cancel_mandate`, `action_close_mandate`, `action_revoke_mandate`, `action_send_and_print`, `action_validate_mandate`, `action_view_paid_invoices`, `action_view_payments_to_collect`
- XPath or positional patches: 0

## Actions

- `account_sepa_direct_debit_mandate_tree_act`: `act_window` Direct Debit Mandates

## Menus

- `account_sepa_direct_debit_customer_mandates_menu`: Direct Debit Mandates

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_sepa_direct_debit/Views]]

