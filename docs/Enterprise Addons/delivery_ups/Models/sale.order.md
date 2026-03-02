<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sale.order

- Module: [[docs/Enterprise Addons/delivery_ups/delivery_ups|delivery_ups]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/sale.py`
- Python classes: `SaleOrder`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 1, `Char` x 1
- Relation fields: 0

## Sample fields

- `partner_ups_carrier_account`: `Char` (compute `_compute_ups_carrier_account`)
- `ups_bill_my_account`: `Boolean` (related `carrier_id.ups_bill_my_account`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_ups_carrier_account`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/delivery_ups/Models]]

<!-- GENERATED:MODEL -->
