---
tags: [odoo, community, generated, views]
---

# views/payment_token_views.xml

- Module: [[docs/Community Addons/payment/payment|payment]]
- Scope: Community Addons
- Source file: `views/payment_token_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `payment_token_search`
- Name: payment.token.search
- Model: `payment.token`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `partner_id`
- XPath or positional patches: 0

### `payment_token_list`
- Name: payment.token.list
- Model: `payment.token`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `company_id`, `partner_id`, `payment_details`, `payment_method_id`, `provider_id`, `provider_ref`
- XPath or positional patches: 0

### `payment_token_form`
- Name: payment.token.form
- Model: `payment.token`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `active`, `company_id`, `partner_id`, `payment_details`, `payment_method_id`, `provider_id`, `provider_ref`
- Buttons: `%(action_payment_transaction_linked_to_token)d`
- XPath or positional patches: 0

## Actions

- `action_payment_token`: `act_window` Payment Tokens

## Navigation

- **Parent:** [[docs/Community Addons/payment/Views]]

