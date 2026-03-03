---
tags: [odoo, community, generated, views]
---

# views/sale_order_line_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `views/sale_order_line_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `sale_order_line_view_kanban`
- Name: sale.order.line.kanban
- Model: `sale.order.line`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 1
- Sample fields: `display_name`
- XPath or positional patches: 0

### `view_sales_order_line_filter`
- Name: sale.order.line.select
- Model: `sale.order.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `order_id`, `order_partner_id`, `product_id`, `salesman_id`
- XPath or positional patches: 0

### `sale_order_line_view_form_readonly`
- Name: sale.order.line.form.readonly
- Model: `sale.order.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `company_id`, `currency_id`, `discount`, `display_name`, `display_type`, `name`, `order_id`, `order_partner_id`, `price_subtotal`, `price_tax`, and 9 more
- XPath or positional patches: 0

### `view_order_line_tree`
- Name: sale.order.line.list
- Model: `sale.order.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `currency_id`, `name`, `order_id`, `order_partner_id`, `price_subtotal`, `product_uom_id`, `product_uom_qty`, `qty_delivered`, `qty_invoiced`, `qty_to_invoice`, and 1 more
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

