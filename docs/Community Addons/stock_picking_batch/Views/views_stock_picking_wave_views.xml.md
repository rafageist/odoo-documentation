---
tags: [odoo, community, generated, views]
---

# views/stock_picking_wave_views.xml

- Module: [[docs/Community Addons/stock_picking_batch/stock_picking_batch|stock_picking_batch]]
- Scope: Community Addons
- Source file: `views/stock_picking_wave_views.xml`
- Views: 3
- Actions: 3
- Menus: 1
- Rules: 0

## View records

### `stock_picking_type_kanban_batch`
- Name: picking.type.kanban.batch
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock.stock_picking_type_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `count_picking_batch`, `count_picking_wave`
- Buttons: `action_batch`
- XPath or positional patches: 4

### `stock_picking_wave_kanban`
- Name: stock.picking.wave.kanban
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_kanban`
- Root tag: `xpath`
- Field references: 0
- Buttons: `stock_picking_batch.action_prepare_wave`
- XPath or positional patches: 2

### `stock_picking_wave_tree`
- Name: stock.picking.wave.list
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_tree`
- Root tag: `xpath`
- Field references: 0
- Buttons: `stock_picking_batch.action_prepare_wave`
- XPath or positional patches: 2

## Actions

- `action_picking_tree_wave`: `act_window` Wave Transfers
- `action_prepare_wave`: `act_window` Prepare Wave
- `action_prepare_wave_for_picking_type`: `act_window` Prepare Wave

## Menus

- `stock_picking_wave_menu`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/stock_picking_batch/Views]]

