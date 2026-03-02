<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Community Addons/repair/repair|repair]]
- Scope: Community Addons
- Source file: `views/stock_picking_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `stock_repair_type_kanban`
- Name: stock.picking.type.kanban
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock.stock_picking_type_kanban`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `color`, `count_repair_confirmed`, `count_repair_late`, `count_repair_ready`, `count_repair_under_repair`, `is_favorite`, `kanban_dashboard_graph`, `name`, `warehouse_id`
- Buttons: `get_repair_stock_picking_action_picking_type`
- XPath or positional patches: 2

### `repair_view_picking_form`
- Name: stock.picking.form.inherit.repair
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `nbr_repairs`, `repair_ids`
- Buttons: `action_view_repairs`
- XPath or positional patches: 1

### `repair_view_picking_type_form`
- Name: stock.picking.type.inherit.repair
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock.view_picking_type_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `create_backorder`, `default_product_location_dest_id`, `default_product_location_src_id`, `default_recycle_location_dest_id`, `default_remove_location_dest_id`
- XPath or positional patches: 5

## Actions

- `action_create_repair_order`: `server` Create Repair

## Navigation

- **Parent:** [[docs/Community Addons/repair/Views]]

<!-- GENERATED:VIEWFILE -->
