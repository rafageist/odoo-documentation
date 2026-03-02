<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# stock.picking.type

- Module: [[docs/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/stock_picking_type.py`
- Python classes: `StockPickingType`

## Field footprint

- Detected fields: 12
- Field types: `Boolean` x 8, `Selection` x 4
- Relation fields: 0

## Sample fields

- `barcode_allow_extra_product`: `Boolean` (comodel `Allow extra products`)
- `barcode_validation_after_dest_location`: `Boolean` (comodel `Force a destination for all products`)
- `barcode_validation_all_product_packed`: `Boolean` (comodel `Force all products to be packed`)
- `barcode_validation_full`: `Boolean` (comodel `Allow full picking validation`)
- `is_barcode_picking_type`: `Boolean` (compute `_compute_is_barcode_picking_type`)
- `restrict_put_in_pack`: `Selection`
- `restrict_scan_dest_location`: `Selection`
- `restrict_scan_product`: `Boolean` (comodel `Force Product scan?`)
- `restrict_scan_source_location`: `Selection`
- `restrict_scan_tracking_number`: `Selection`
- `show_barcode_validation`: `Boolean` (compute `_compute_show_barcode_validation`)
- `show_reserved_sns`: `Boolean` (comodel `Show reserved lots/SN`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_is_barcode_picking_type`, `_compute_show_barcode_validation`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode/Models]]

<!-- GENERATED:MODEL -->
