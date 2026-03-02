<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/batch_gantt.xml

- Module: [[docs/Enterprise Addons/stock_fleet_enterprise/stock_fleet_enterprise|stock_fleet_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/batch_gantt.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_stock_picking_batch_gantt`
- Name: stock.picking.batch.gantt
- Model: `stock.picking.batch`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 4
- Sample fields: `driver_id`, `scheduled_date`, `state`, `user_id`
- Buttons: `action_open_batch_from_gantt_view`
- XPath or positional patches: 0

### `stock_picking_batch_view_kanban`
- Name: stock.picking.batch.view.kanban
- Model: `stock.picking.batch`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `company_id`, `dock_id`, `end_date`, `name`, `scheduled_date`, `state`, `user_id`
- XPath or positional patches: 0

## Actions

- `stock_picking_batch.stock_picking_batch_action`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_fleet_enterprise/Views]]

<!-- GENERATED:VIEWFILE -->
