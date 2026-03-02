<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# stock.quant

- Module: [[docs/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/stock_quant.py`
- Python classes: `StockQuant`

## Field footprint

- Detected fields: 3
- Field types: `Char` x 2, `Image` x 1
- Relation fields: 0

## Sample fields

- `dummy_id`: `Char` (compute `_compute_dummy_id`)
- `image_1920`: `Image` (related `product_id.image_1920`)
- `product_reference_code`: `Char` (related `product_id.code`)

## Method hints

- Detected methods: 10
- Action methods: `action_client_action`, `action_validate`
- Compute methods: `_compute_dummy_id`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode/Models]]

<!-- GENERATED:MODEL -->
