<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.move.line

- Module: [[docs/Community Addons/stock_landed_costs/stock_landed_costs|stock_landed_costs]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/account_move.py`
- Python classes: `AccountMoveLine`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `is_landed_costs_line`: `Boolean`
- `product_type`: `Selection` (related `product_id.type`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: none
- Onchange methods: `_onchange_is_landed_costs_line`, `_onchange_product_id_landed_costs`

## Navigation

- **Parent:** [[docs/Community Addons/stock_landed_costs/Models]]

<!-- GENERATED:MODEL -->
