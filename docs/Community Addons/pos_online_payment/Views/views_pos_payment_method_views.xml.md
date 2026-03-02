<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/pos_payment_method_views.xml

- Module: [[docs/Community Addons/pos_online_payment/pos_online_payment|pos_online_payment]]
- Scope: Community Addons
- Source file: `views/pos_payment_method_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `pos_payment_method_view_tree_inherit_pos_online_payment`
- Name: pos.payment.method.list.inherit.pos_online_payment
- Model: `pos.payment.method`
- Type: inferred from arch
- Inherits: `point_of_sale.pos_payment_method_view_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `has_an_online_payment_provider`, `is_online_payment`
- XPath or positional patches: 2

### `pos_payment_method_view_form_inherit_pos_online_payment`
- Name: pos.payment.method.form.inherit.pos_online_payment
- Model: `pos.payment.method`
- Type: inferred from arch
- Inherits: `point_of_sale.pos_payment_method_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `has_an_online_payment_provider`, `is_online_payment`, `online_payment_provider_ids`
- Buttons: `%(payment.action_payment_provider)d`
- XPath or positional patches: 8

## Navigation

- **Parent:** [[docs/Community Addons/pos_online_payment/Views]]

<!-- GENERATED:VIEWFILE -->
