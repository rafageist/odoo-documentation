---
tags: [odoo, enterprise, generated, views]
---

# views/stock_barcode_picking_batch.xml

- Module: [[docs/Enterprise Addons/stock_barcode_picking_batch/stock_barcode_picking_batch|stock_barcode_picking_batch]]
- Scope: Enterprise Addons
- Source file: `views/stock_barcode_picking_batch.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `stock_picking_batch_form`
- Name: stock.picking.batch.form.inherit.stock.barcode
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_client_action`
- XPath or positional patches: 1

### `stock_barcode_batch_picking_view_kanban`
- Name: stock.picking.batch.kanban
- Model: `stock.picking.batch`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `company_id`, `description`, `move_line_ids`, `name`, `picking_type_id`, `scheduled_date`, `state`, `user_id`
- XPath or positional patches: 0

### `stock_barcode_batch_picking_view_info`
- Name: stock.picking.batch.form.view.barcode
- Model: `stock.picking.batch`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `allowed_picking_ids`, `company_id`, `description_picking`, `location_id`, `move_ids`, `name`, `picking_ids`, `picking_type_id`, `product_id`, `product_uom_qty`, and 4 more
- Buttons: `action_unbatch`, `action_view_reception_report`
- XPath or positional patches: 0

## Actions

- `stock_barcode_batch_picking_action_kanban`: `act_window` Batch Transfers

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode_picking_batch/Views]]

