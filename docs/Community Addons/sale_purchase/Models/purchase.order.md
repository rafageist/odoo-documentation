<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# purchase.order

- Module: [[docs/Community Addons/sale_purchase/sale_purchase|sale_purchase]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/purchase_order.py`
- Python classes: `PurchaseOrder`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 1, `Integer` x 1
- Relation fields: 0

## Sample fields

- `has_sale_order`: `Boolean` (comodel `Technical field for whether the purchase order has associated sale orders`, compute `_compute_sale_order_count`)
- `sale_order_count`: `Integer` (comodel `Number of Source Sale`, compute `_compute_sale_order_count`)

## Method hints

- Detected methods: 6
- Action methods: `action_view_sale_orders`
- Compute methods: `_compute_dest_address_id`, `_compute_sale_order_count`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/sale_purchase/Models]]

<!-- GENERATED:MODEL -->
