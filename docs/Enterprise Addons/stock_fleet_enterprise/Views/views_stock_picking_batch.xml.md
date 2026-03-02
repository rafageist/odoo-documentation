<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_batch.xml

- Module: [[docs/Enterprise Addons/stock_fleet_enterprise/stock_fleet_enterprise|stock_fleet_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_batch.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_picking_batch_view_form_plan_batch`
- Name: stock.picking.batch.view.form.plan.batch
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `end_date`, `move_line_ids`, `state`
- Buttons: `action_picking_map_view`
- XPath or positional patches: 7

### `stock_picking_batch_form`
- Name: stock.picking.batch.form.inherit.stock.fleet.enterprise
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_form`
- Root tag: `data`
- Field references: 0
- Buttons: `action_picking_map_view`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_fleet_enterprise/Views]]

<!-- GENERATED:VIEWFILE -->
