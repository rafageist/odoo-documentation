<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Enterprise Addons/sale_amazon/sale_amazon|sale_amazon]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_sales_order_filter`
- Name: amazon.order.search
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sales_order_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `amazon_order_ref`, `name`
- XPath or positional patches: 0

### `amazon_order_view_form`
- Name: amazon.order.form
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `div`
- Field references: 1
- Sample fields: `amazon_order_ref`
- Buttons: `action_lock`
- XPath or positional patches: 3

### `sale_order_tree`
- Name: amazon.order.list
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.sale_order_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `amazon_order_ref`, `name`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_amazon/Views]]

<!-- GENERATED:VIEWFILE -->
