<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_picking_batch.xml

- Module: [[docs/Community Addons/stock_fleet/stock_fleet|stock_fleet]]
- Scope: Community Addons
- Source file: `views/stock_picking_batch.xml`
- Views: 6
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_picking_batch_kanban`
- Name: stock.picking.batch.kanban.inherit.stock.fleet
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_kanban`
- Root tag: `data`
- Field references: 4
- Sample fields: `dock_id`, `scheduled_date`, `state`, `user_id`
- XPath or positional patches: 1

### `stock_picking_batch_filter`
- Name: stock.picking.batch.filter.inherit.stock.fleet
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_filter`
- Root tag: `field`
- Field references: 4
- Sample fields: `dock_id`, `driver_id`, `user_id`, `vehicle_id`
- XPath or positional patches: 3

### `stock_picking_batch_tree`
- Name: stock.picking.batch.list.inherit.stock.fleet
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_tree`
- Root tag: `data`
- Field references: 6
- Sample fields: `dock_id`, `used_volume_percentage`, `used_weight_percentage`, `user_id`, `vehicle_category_id`, `vehicle_id`
- XPath or positional patches: 0

### `stock_picking_batch_form`
- Name: stock.picking.batch.form.inherit.stock.fleet
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_form`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `dock_id`, `estimated_shipping_volume`, `estimated_shipping_weight`, `used_volume_percentage`, `used_weight_percentage`, `vehicle_category_id`, `vehicle_id`, `volume_uom_name`, `weight_uom_name`
- XPath or positional patches: 1

### `stock_picking_batch_graph`
- Name: stock.picking.batch.graph
- Model: `stock.picking.batch`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `scheduled_date`, `vehicle_category_id`
- XPath or positional patches: 0

### `stock_picking_batch_pivot`
- Name: stock.picking.batch.pivot
- Model: `stock.picking.batch`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `scheduled_date`, `vehicle_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/stock_fleet/Views]]

<!-- GENERATED:VIEWFILE -->
