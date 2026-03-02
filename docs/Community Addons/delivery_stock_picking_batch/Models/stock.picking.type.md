<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.picking.type

- Module: [[docs/Community Addons/delivery_stock_picking_batch/delivery_stock_picking_batch|delivery_stock_picking_batch]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/stock_picking.py`
- Python classes: `StockPickingType`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 1, `Integer` x 1
- Relation fields: 0

## Sample fields

- `batch_group_by_carrier`: `Boolean` (comodel `Carrier`)
- `batch_max_weight`: `Integer` (comodel `Maximum weight`)
- `weight_uom_name`: `Char` (compute `_compute_weight_uom_name`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_weight_uom_name`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/delivery_stock_picking_batch/Models]]

<!-- GENERATED:MODEL -->
