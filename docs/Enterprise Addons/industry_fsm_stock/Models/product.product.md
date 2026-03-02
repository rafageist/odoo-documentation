<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# product.product

- Module: [[docs/Enterprise Addons/industry_fsm_stock/industry_fsm_stock|industry_fsm_stock]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/product.py`
- Python classes: `ProductProduct`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 2, `Integer` x 1
- Relation fields: 0

## Sample fields

- `quantity_decreasable`: `Boolean` (compute `_compute_quantity_decreasable`)
- `quantity_decreasable_sum`: `Integer` (compute `_compute_quantity_decreasable`)
- `serial_missing`: `Boolean` (compute `_compute_serial_missing`)

## Method hints

- Detected methods: 6
- Action methods: `action_assign_serial`, `action_product_forecast_report`
- Compute methods: `_compute_quantity_decreasable`, `_compute_serial_missing`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_stock/Models]]

<!-- GENERATED:MODEL -->
