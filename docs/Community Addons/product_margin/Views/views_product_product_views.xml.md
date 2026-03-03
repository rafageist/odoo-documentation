---
tags: [odoo, community, generated, views]
---

# views/product_product_views.xml

- Module: [[docs/Community Addons/product_margin/product_margin|product_margin]]
- Scope: Community Addons
- Source file: `views/product_product_views.xml`
- Views: 3
- Actions: 0
- Menus: 1
- Rules: 0

## View records

### `view_product_margin_tree`
- Name: product.margin.list
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 16
- Sample fields: `categ_id`, `company_id`, `default_code`, `expected_margin`, `expected_margin_rate`, `name`, `purchase_num_invoiced`, `sale_avg_price`, `sale_num_invoiced`, `sales_gap`, and 6 more
- XPath or positional patches: 0

### `view_product_margin_form`
- Name: product.margin.form.inherit
- Model: `product.product`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `date_from`, `date_to`, `default_code`, `expected_margin`, `expected_margin_rate`, `invoice_state`, `list_price`, `name`, `normal_cost`, `purchase_avg_price`, and 11 more
- XPath or positional patches: 0

### `view_product_margin_graph`
- Name: product.margin.graph
- Model: `product.product`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `product_tmpl_id`, `total_margin`
- XPath or positional patches: 0

## Menus

- `menu_action_product_margin`: Product Margins…

## Navigation

- **Parent:** [[docs/Community Addons/product_margin/Views]]

