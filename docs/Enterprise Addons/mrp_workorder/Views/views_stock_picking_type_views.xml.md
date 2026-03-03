---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_type_views.xml

- Module: [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_type_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_picking_type_form_inherit_mrp_workorder`
- Name: Operation Types
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock.view_picking_type_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `auto_close_production`, `prefill_shop_floor_lots`
- XPath or positional patches: 1

### `stock_picking_type_view_kanban`
- Name: stock.picking.view.kanban
- Model: `stock.picking.type`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `color`, `count_mo_todo`, `name`, `warehouse_id`
- Buttons: `%(mrp.mrp_workcenter_kanban_action)d`
- XPath or positional patches: 0

## Actions

- `mrp_stock_picking_type_action`: `act_window` Overview

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_workorder/Views]]

