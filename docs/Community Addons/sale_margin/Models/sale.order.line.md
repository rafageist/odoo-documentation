<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# sale.order.line

- Module: [[docs/Community Addons/sale_margin/sale_margin|sale_margin]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/sale_order_line.py`
- Python classes: `SaleOrderLine`

## Field footprint

- Detected fields: 3
- Field types: `Float` x 3
- Relation fields: 0

## Sample fields

- `margin`: `Float` (comodel `Margin`, compute `_compute_margin`, store `True`)
- `margin_percent`: `Float` (comodel `Margin (%)`, compute `_compute_margin`, store `True`)
- `purchase_price`: `Float` (compute `_compute_purchase_price`, store `True`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_margin`, `_compute_purchase_price`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/sale_margin/Models]]

<!-- GENERATED:MODEL -->
