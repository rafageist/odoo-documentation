---
tags: [odoo, community, generated, views]
---

# views/stock_picking_view.xml

- Module: [[docs/Community Addons/stock_fleet/stock_fleet|stock_fleet]]
- Scope: Community Addons
- Source file: `views/stock_picking_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_picking_tree_inherit_stock_fleet`
- Name: stock.picking.list.inherit.stock.transport
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_view_batch_tree_ref`
- Root tag: `field`
- Field references: 1
- Sample fields: `zip`
- XPath or positional patches: 0

### `vpicktree`
- Name: stock.picking.list.inherit.stock.fleet
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `field`
- Field references: 4
- Sample fields: `picking_type_id`, `shipping_volume`, `shipping_weight`, `zip`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/stock_fleet/Views]]

