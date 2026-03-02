<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.supplierinfo

- Module: [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/product.py`
- Python classes: `ProductSupplierinfo`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 1, `Date` x 1
- Relation fields: 0

## Sample fields

- `last_purchase_date`: `Date` (comodel `Last Purchase`, compute `_compute_last_purchase_date`)
- `show_set_supplier_button`: `Boolean` (comodel `Show Set Supplier Button`, compute `_compute_show_set_supplier_button`)

## Method hints

- Detected methods: 4
- Action methods: `action_set_supplier`
- Compute methods: `_compute_display_name`, `_compute_last_purchase_date`, `_compute_show_set_supplier_button`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/purchase_stock/Models]]

<!-- GENERATED:MODEL -->
