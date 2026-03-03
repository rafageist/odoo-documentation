---
tags: [odoo, community, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Community Addons/sale_stock/sale_stock|sale_stock]]
- Scope: Community Addons
- Source file: `views/sale_order_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `sale_stock_sale_order_view_search_inherit`
- Name: sale_stock.sale.order.search.inherit
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.sale_order_view_search_inherit_sale`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_order_tree`
- Name: sale.order.list.inherit.sale.stock
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `commitment_date`, `delivery_status`, `invoice_status`
- XPath or positional patches: 0

### `sale_order_tree`
- Name: sale.order.list.inherit.sale.stock
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.sale_order_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `tag_ids`, `warehouse_id`
- XPath or positional patches: 0

### `view_order_form_inherit_sale_stock`
- Name: sale.order.form.sale.stock
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `button`
- Field references: 11
- Sample fields: `commitment_date`, `delivery_count`, `delivery_status`, `effective_date`, `expected_date`, `incoterm`, `incoterm_location`, `json_popover`, `picking_policy`, `route_ids`, and 1 more
- Buttons: `action_view_delivery`, `action_view_invoice`
- XPath or positional patches: 9

## Navigation

- **Parent:** [[docs/Community Addons/sale_stock/Views]]

