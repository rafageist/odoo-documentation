<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.move.line

- Module: [[docs/Community Addons/product_expiry/product_expiry|product_expiry]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/stock_move_line.py`
- Python classes: `StockMoveLine`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 2, `Datetime` x 2
- Relation fields: 0

## Sample fields

- `expiration_date`: `Datetime` (compute `_compute_expiration_date`, store `True`)
- `is_expired`: `Boolean` (related `lot_id.product_expiry_alert`)
- `removal_date`: `Datetime` (compute `_compute_removal_date`, store `True`)
- `use_expiration_date`: `Boolean` (related `product_id.use_expiration_date`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_expiration_date`, `_compute_removal_date`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/product_expiry/Models]]

<!-- GENERATED:MODEL -->
