---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_line_views.xml

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_line_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `sale_subscription_sales_order_line_filter`
- Name: sale.subscription.sale.order.line.select
- Model: `sale.order.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `name`, `order_id`, `order_partner_id`
- XPath or positional patches: 0

### `sale_subscription_sale_order_line_list`
- Name: sale.subscription.plan.inherit.line.tree
- Model: `sale.order.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `name`, `next_invoice_date`, `order_id`, `order_partner_id`, `price_unit`, `pricelist_id`, `product_template_variant_value_ids`, `subscription_end_date`, `subscription_start_date`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Views]]

