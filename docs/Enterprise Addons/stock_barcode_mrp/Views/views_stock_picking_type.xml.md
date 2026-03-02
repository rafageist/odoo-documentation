<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_type.xml

- Module: [[docs/Enterprise Addons/stock_barcode_mrp/stock_barcode_mrp|stock_barcode_mrp]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_type.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_picking_type_form`
- Name: Operation Types
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock_barcode.stock_barcode_view_picking_type_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `barcode_validation_all_product_packed`, `barcode_validation_full`, `restrict_put_in_pack`
- XPath or positional patches: 0

### `stock_mrp_picking_type_kanban`
- Name: stock.mrp.picking.type.kanban
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock_barcode.stock_picking_type_kanban`
- Root tag: `div`
- Field references: 2
- Sample fields: `count_mo_confirmed`, `count_picking_ready`
- XPath or positional patches: 1

## Actions

- `stock_barcode.stock_picking_type_action_kanban`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode_mrp/Views]]

<!-- GENERATED:VIEWFILE -->
