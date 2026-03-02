<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# sale.order

- Module: [[docs/Community Addons/sale_margin/sale_margin|sale_margin]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/sale_order.py`
- Python classes: `SaleOrder`

## Field footprint

- Detected fields: 2
- Field types: `Float` x 1, `Monetary` x 1
- Relation fields: 0

## Sample fields

- `margin`: `Monetary` (comodel `Margin`, compute `_compute_margin`, store `True`)
- `margin_percent`: `Float` (comodel `Margin (%)`, compute `_compute_margin`, store `True`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_margin`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/sale_margin/Models]]

<!-- GENERATED:MODEL -->
