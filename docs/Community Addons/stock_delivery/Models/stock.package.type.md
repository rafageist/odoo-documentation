<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.package.type

- Module: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/stock_package_type.py`
- Python classes: `StockPackageType`

## Field footprint

- Detected fields: 2
- Field types: `Char` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `package_carrier_type`: `Selection`
- `shipper_package_code`: `Char` (comodel `Carrier Code`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_length_uom_name`
- Onchange methods: `_onchange_carrier_type`

## Navigation

- **Parent:** [[docs/Community Addons/stock_delivery/Models]]

<!-- GENERATED:MODEL -->
