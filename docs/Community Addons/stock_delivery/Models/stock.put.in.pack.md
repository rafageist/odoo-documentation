<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.put.in.pack

- Module: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `wizard/stock_put_in_pack.py`
- Python classes: `StockPutInPack`

## Field footprint

- Detected fields: 3
- Field types: `Char` x 2, `Float` x 1
- Relation fields: 0

## Sample fields

- `package_carrier_type`: `Char` (comodel `Carrier Type`)
- `shipping_weight`: `Float` (comodel `Shipping Weight`, compute `_compute_shipping_weight`, store `True`)
- `weight_uom_name`: `Char` (compute `_compute_weight_uom_name`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_shipping_weight`, `_compute_weight_uom_name`
- Onchange methods: `_onchange_package_type_weight`

## Navigation

- **Parent:** [[docs/Community Addons/stock_delivery/Models]]

<!-- GENERATED:MODEL -->
