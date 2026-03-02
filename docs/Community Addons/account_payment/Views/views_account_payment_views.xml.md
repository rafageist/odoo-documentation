<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_payment_views.xml

- Module: [[docs/Community Addons/account_payment/account_payment|account_payment]]
- Scope: Community Addons
- Source file: `views/account_payment_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_payment_form_inherit_payment`
- Name: view.account.payment.form.inherit.payment
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_form`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `amount_available_for_refund`, `payment_method_code`, `payment_method_line_id`, `payment_token_id`, `payment_transaction_id`, `refunds_count`, `source_payment_id`, `suitable_payment_token_ids`, `use_electronic_payment_method`
- Buttons: `action_refund_wizard`, `action_view_refunds`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Community Addons/account_payment/Views]]

<!-- GENERATED:VIEWFILE -->
