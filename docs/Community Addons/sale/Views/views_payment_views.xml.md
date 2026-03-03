---
tags: [odoo, community, generated, views]
---

# views/payment_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `views/payment_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `transaction_form_inherit_sale`
- Name: payment.transaction.form.inherit.sale.payment
- Model: `payment.transaction`
- Type: inferred from arch
- Inherits: `payment.payment_transaction_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sale_order_ids_nbr`
- Buttons: `action_view_sales_orders`
- XPath or positional patches: 1

### `payment_provider_form`
- Name: payment.provider.form.inherit.sale
- Model: `payment.provider`
- Type: inferred from arch
- Inherits: `payment.payment_provider_form`
- Root tag: `group`
- Field references: 1
- Sample fields: `so_reference_type`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

