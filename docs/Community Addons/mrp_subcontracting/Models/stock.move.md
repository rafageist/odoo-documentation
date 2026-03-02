<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.move

- Module: [[docs/Community Addons/mrp_subcontracting/mrp_subcontracting|mrp_subcontracting]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/stock_move.py`
- Python classes: `StockMove`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 2
- Relation fields: 0

## Sample fields

- `is_subcontract`: `Boolean` (comodel `The move is a subcontract receipt`)
- `show_subcontracting_details_visible`: `Boolean` (compute `_compute_show_subcontracting_details_visible`)

## Method hints

- Detected methods: 20
- Action methods: `action_show_details`, `action_show_subcontract_details`
- Compute methods: `_compute_is_quantity_done_editable`, `_compute_show_info`, `_compute_show_subcontracting_details_visible`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/mrp_subcontracting/Models]]

<!-- GENERATED:MODEL -->
