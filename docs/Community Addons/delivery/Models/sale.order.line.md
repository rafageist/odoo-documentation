<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# sale.order.line

- Module: [[docs/Community Addons/delivery/delivery|delivery]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/sale_order_line.py`
- Python classes: `SaleOrderLine`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 2, `Float` x 1
- Relation fields: 0

## Sample fields

- `is_delivery`: `Boolean`
- `product_qty`: `Float` (compute `_compute_product_qty`)
- `recompute_delivery_price`: `Boolean` (related `order_id.recompute_delivery_price`)

## Method hints

- Detected methods: 7
- Action methods: none
- Compute methods: `_compute_pricelist_item_id`, `_compute_product_qty`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/delivery/Models]]

<!-- GENERATED:MODEL -->
