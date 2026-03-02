<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.template

- Module: [[docs/Community Addons/purchase/purchase|purchase]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/product.py`
- Python classes: `ProductTemplate`

## Field footprint

- Detected fields: 3
- Field types: `Float` x 1, `Selection` x 1, `Text` x 1
- Relation fields: 0

## Sample fields

- `purchase_line_warn_msg`: `Text` (comodel `Message for Purchase Order Line`)
- `purchase_method`: `Selection` (compute `_compute_purchase_method`, store `True`)
- `purchased_product_qty`: `Float` (compute `_compute_purchased_product_qty`)

## Method hints

- Detected methods: 5
- Action methods: `action_view_po`
- Compute methods: `_compute_purchase_method`, `_compute_purchased_product_qty`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/purchase/Models]]

<!-- GENERATED:MODEL -->
