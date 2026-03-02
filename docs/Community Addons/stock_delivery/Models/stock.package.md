<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.package

- Module: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/stock_package.py`
- Python classes: `StockPackage`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Char` x 1, `Float` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `package_carrier_type`: `Selection` (related `package_type_id.package_carrier_type`)
- `weight`: `Float` (compute `_compute_weight`)
- `weight_is_kg`: `Boolean` (comodel `Technical field indicating whether weight uom is kg or not (i.e. lb)`, compute `_compute_weight_is_kg`)
- `weight_uom_name`: `Char` (compute `_compute_weight_uom_name`)
- `weight_uom_rounding`: `Float` (comodel `Technical field indicating weight's number of decimal places`, compute `_compute_weight_is_kg`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_weight`, `_compute_weight_is_kg`, `_compute_weight_uom_name`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/stock_delivery/Models]]

<!-- GENERATED:MODEL -->
