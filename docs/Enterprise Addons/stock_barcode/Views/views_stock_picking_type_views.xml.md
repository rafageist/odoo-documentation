---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_type_views.xml

- Module: [[docs/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_type_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `stock_barcode_view_picking_type_form`
- Name: Operation Types
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock.view_picking_type_form`
- Root tag: `field`
- Field references: 16
- Sample fields: `barcode`, `barcode_allow_extra_product`, `barcode_validation_after_dest_location`, `barcode_validation_all_product_packed`, `barcode_validation_full`, `color`, `is_barcode_picking_type`, `restrict_put_in_pack`, `restrict_scan_dest_location`, `restrict_scan_product`, and 6 more
- XPath or positional patches: 2

### `stock_picking_type_kanban`
- Name: stock.picking.type.kanban
- Model: `stock.picking.type`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `code`, `color`, `count_picking_ready`, `is_barcode_picking_type`, `name`, `warehouse_id`
- XPath or positional patches: 0

## Actions

- `stock_picking_type_action_kanban`: `act_window` Operations

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode/Views]]

