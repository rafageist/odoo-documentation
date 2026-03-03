---
tags: [odoo, community, generated, views]
---

# views/pos_payment_views.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/pos_payment_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_pos_payment_search`
- Name: pos.payment.search.view
- Model: `pos.payment`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `amount`, `name`, `pos_order_id`
- XPath or positional patches: 0

### `view_pos_payment_tree`
- Name: pos.payment.list
- Model: `pos.payment`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `amount`, `currency_id`, `payment_date`, `payment_method_id`, `pos_order_id`, `user_id`
- XPath or positional patches: 0

### `view_pos_payment_form`
- Name: pos.payment.form
- Model: `pos.payment`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `amount`, `card_brand`, `card_no`, `card_type`, `cardholder_name`, `payment_method_authcode`, `payment_method_id`, `payment_method_issuer_bank`, `payment_method_payment_mode`, `payment_ref_no`, and 3 more
- XPath or positional patches: 0

## Actions

- `action_pos_payment_form`: `act_window` Payments

## Menus

- `menu_pos_payment`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

