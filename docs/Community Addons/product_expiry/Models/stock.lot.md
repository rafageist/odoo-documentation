<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.lot

- Module: [[docs/Community Addons/product_expiry/product_expiry|product_expiry]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/production_lot.py`
- Python classes: `StockLot`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 3, `Datetime` x 4
- Relation fields: 0

## Sample fields

- `alert_date`: `Datetime` (compute `_compute_dates`, store `True`)
- `expiration_date`: `Datetime` (compute `_compute_expiration_date`, store `True`)
- `product_expiry_alert`: `Boolean` (compute `_compute_product_expiry_alert`)
- `product_expiry_reminded`: `Boolean`
- `removal_date`: `Datetime` (compute `_compute_dates`, store `True`)
- `use_date`: `Datetime` (compute `_compute_dates`, store `True`)
- `use_expiration_date`: `Boolean` (related `product_id.use_expiration_date`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_dates`, `_compute_display_name`, `_compute_expiration_date`, `_compute_product_expiry_alert`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/product_expiry/Models]]

<!-- GENERATED:MODEL -->
