<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# stock.move.line

- Module: [[docs/Enterprise Addons/stock_barcode_mrp/stock_barcode_mrp|stock_barcode_mrp]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/stock_move_line.py`
- Python classes: `StockMoveLine`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 2
- Relation fields: 0

## Sample fields

- `manual_consumption`: `Boolean` (related `move_id.manual_consumption`)
- `pick_type_create_components_lots`: `Boolean` (related `picking_type_id.use_create_components_lots`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_hide_lot_name`, `_compute_parent_location_id`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode_mrp/Models]]

<!-- GENERATED:MODEL -->
