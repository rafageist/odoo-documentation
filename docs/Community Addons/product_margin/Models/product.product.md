<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.product

- Module: [[docs/Community Addons/product_margin/product_margin|product_margin]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/product_product.py`
- Python classes: `ProductProduct`

## Field footprint

- Detected fields: 17
- Field types: `Date` x 2, `Float` x 14, `Selection` x 1
- Relation fields: 0

## Sample fields

- `date_from`: `Date` (compute `_compute_product_margin_fields_values`)
- `date_to`: `Date` (compute `_compute_product_margin_fields_values`)
- `expected_margin`: `Float` (compute `_compute_product_margin_fields_values`)
- `expected_margin_rate`: `Float` (compute `_compute_product_margin_fields_values`)
- `invoice_state`: `Selection` (compute `_compute_product_margin_fields_values`)
- `normal_cost`: `Float` (compute `_compute_product_margin_fields_values`)
- `purchase_avg_price`: `Float` (compute `_compute_product_margin_fields_values`)
- `purchase_gap`: `Float` (compute `_compute_product_margin_fields_values`)
- `purchase_num_invoiced`: `Float` (compute `_compute_product_margin_fields_values`)
- `sale_avg_price`: `Float` (compute `_compute_product_margin_fields_values`)
- `sale_expected`: `Float` (compute `_compute_product_margin_fields_values`)
- `sale_num_invoiced`: `Float` (compute `_compute_product_margin_fields_values`)
- `sales_gap`: `Float` (compute `_compute_product_margin_fields_values`)
- `total_cost`: `Float` (compute `_compute_product_margin_fields_values`)
- `total_margin`: `Float` (compute `_compute_product_margin_fields_values`)
- `total_margin_rate`: `Float` (compute `_compute_product_margin_fields_values`)
- `turnover`: `Float` (compute `_compute_product_margin_fields_values`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_product_margin_fields_values`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/product_margin/Models]]

<!-- GENERATED:MODEL -->
