<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# purchase.order

- Module: [[docs/Community Addons/stock_dropshipping/stock_dropshipping|stock_dropshipping]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/purchase.py`
- Python classes: `PurchaseOrder`

## Field footprint

- Detected fields: 1
- Field types: `Integer` x 1
- Relation fields: 0

## Sample fields

- `dropship_picking_count`: `Integer` (comodel `Dropship Count`, compute `_compute_incoming_picking_count`)

## Method hints

- Detected methods: 4
- Action methods: `action_view_dropship`, `action_view_picking`
- Compute methods: `_compute_incoming_picking_count`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/stock_dropshipping/Models]]

<!-- GENERATED:MODEL -->
