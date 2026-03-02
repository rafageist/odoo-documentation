<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Enterprise Addons/sale_shopee/sale_shopee|sale_shopee]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_sales_order_filter`
- Name: shopee.order.search
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sales_order_filter`
- Root tag: `field`
- Field references: 3
- Sample fields: `name`, `shopee_order_ref`, `shopee_shop_id`
- XPath or positional patches: 0

### `view_order_form`
- Name: shopee.order.form
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `div`
- Field references: 2
- Sample fields: `shopee_order_ref`, `shopee_shop_id`
- Buttons: `action_lock`
- XPath or positional patches: 3

### `sale_order_tree`
- Name: shopee.order.list
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.sale_order_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `name`, `shopee_order_ref`, `shopee_shop_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_shopee/Views]]

<!-- GENERATED:VIEWFILE -->
