<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_views.xml

- Module: [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]]
- Scope: Community Addons
- Source file: `views/stock_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_warehouse_orderpoint_tree_editable_inherited_mrp`
- Name: stock.warehouse.orderpoint.list.editable.inherit.mrp
- Model: `stock.warehouse.orderpoint`
- Type: inferred from arch
- Inherits: `stock.view_warehouse_orderpoint_tree_editable`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `show_supplier`, `supplier_id`, `supplier_id_placeholder`
- XPath or positional patches: 1

### `view_warehouse_inherited`
- Name: Stock Warehouse Inherited
- Model: `stock.warehouse`
- Type: inferred from arch
- Inherits: `stock.view_warehouse`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `buy_to_resupply`
- XPath or positional patches: 2

### `stock_move_purchase`
- Name: stock.move.form
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_move_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `purchase_line_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/purchase_stock/Views]]

<!-- GENERATED:VIEWFILE -->
