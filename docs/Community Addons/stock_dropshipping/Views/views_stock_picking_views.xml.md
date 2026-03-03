---
tags: [odoo, community, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Community Addons/stock_dropshipping/stock_dropshipping|stock_dropshipping]]
- Scope: Community Addons
- Source file: `views/stock_picking_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `stock_picking_type_kanban`
- Name: stock.picking.type.kanban.inherit.dropshipping
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock.stock_picking_type_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_picking_internal_search_inherit_stock_dropshipping`
- Name: stock.picking.search
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_internal_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `action_picking_tree_dropship`: `act_window` Dropships

## Menus

- `dropship_picking`: Dropships

## Navigation

- **Parent:** [[docs/Community Addons/stock_dropshipping/Views]]

