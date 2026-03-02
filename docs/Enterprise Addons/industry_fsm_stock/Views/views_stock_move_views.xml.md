<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_move_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm_stock/industry_fsm_stock|industry_fsm_stock]]
- Scope: Enterprise Addons
- Source file: `views/stock_move_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_move_kanban_picking_redirect`
- Name: stock.move.kanban.picking.redirect
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `location_id`, `product_id`, `product_uom`, `product_uom_qty`, `quantity`, `state`
- XPath or positional patches: 0

### `view_move_tree_picking_redirect`
- Name: stock.move.list.picking.redirect
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_move_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_stock/Views]]

<!-- GENERATED:VIEWFILE -->
