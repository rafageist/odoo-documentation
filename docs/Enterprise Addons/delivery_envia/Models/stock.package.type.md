<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# stock.package.type

- Module: [[docs/Enterprise Addons/delivery_envia/delivery_envia|delivery_envia]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/stock_package_type.py`
- Python classes: `StockPackageType`

## Field footprint

- Detected fields: 3
- Field types: `Char` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `envia_mail_type`: `Selection`
- `package_carrier_type`: `Selection`
- `shipper_package_code`: `Char` (compute `_compute_package_code`, store `True`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_length_uom_name`, `_compute_package_code`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/delivery_envia/Models]]

<!-- GENERATED:MODEL -->
