<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.quant

- Module: [[docs/Community Addons/product_expiry/product_expiry|product_expiry]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/stock_quant.py`
- Python classes: `StockQuant`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 1, `Datetime` x 2, `Float` x 1
- Relation fields: 0

## Sample fields

- `available_quantity`: `Float`
- `expiration_date`: `Datetime` (related `lot_id.expiration_date`, store `True`)
- `removal_date`: `Datetime` (related `lot_id.removal_date`, store `True`)
- `use_expiration_date`: `Boolean` (related `product_id.use_expiration_date`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_available_quantity`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/product_expiry/Models]]

<!-- GENERATED:MODEL -->
