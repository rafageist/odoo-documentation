<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_picking_type.xml

- Module: [[docs/Community Addons/stock_fleet/stock_fleet|stock_fleet]]
- Scope: Community Addons
- Source file: `views/stock_picking_type.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_picking_type_form`
- Name: stock.picking.type.form.inherit.stock_fleet
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock.view_picking_type_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `dispatch_management`, `dock_ids`
- XPath or positional patches: 1

### `stock_picking_type_kanban_inherit_stock_fleet`
- Name: stock.picking.type.kanban.inherit.stock.transport
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock.stock_picking_type_kanban`
- Root tag: `data`
- Field references: 1
- Sample fields: `dispatch_management`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/stock_fleet/Views]]

<!-- GENERATED:VIEWFILE -->
