---
tags: [odoo, enterprise, generated, views]
---

# views/stock_barcode_picking.xml

- Module: [[docs/Enterprise Addons/stock_barcode_picking_batch/stock_barcode_picking_batch|stock_barcode_picking_batch]]
- Scope: Enterprise Addons
- Source file: `views/stock_barcode_picking.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_picking_type_form`
- Name: Operation Types
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock_barcode.stock_barcode_view_picking_type_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `group_lines_by_product`
- XPath or positional patches: 1

### `stock_picking_view_kanban`
- Name: stock.picking.view.kanban.barcode.picking.batch
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock_barcode.stock_picking_view_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `batch_id`, `display_batch_button`
- Buttons: `action_open_batch_picking`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode_picking_batch/Views]]

