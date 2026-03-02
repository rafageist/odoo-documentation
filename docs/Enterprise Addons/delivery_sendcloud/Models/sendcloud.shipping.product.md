<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sendcloud.shipping.product

- Module: [[docs/Enterprise Addons/delivery_sendcloud/delivery_sendcloud|delivery_sendcloud]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/sendcloud_shipping_product.py`
- Python classes: `SendcloudShippingProduct`
- Description: Choose from the available sendcloud shipping products

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 2, `Char` x 3, `Integer` x 2, `Json` x 1
- Relation fields: 0

## Sample fields

- `can_customize_functionalities`: `Boolean` (compute `_compute_can_customize_functionalities`, store `True`)
- `carrier`: `Char`
- `functionalities`: `Json`
- `has_multicollo`: `Boolean` (compute `_compute_has_multicollo`, store `True`)
- `max_weight`: `Integer`
- `min_weight`: `Integer`
- `name`: `Char`
- `sendcloud_code`: `Char`

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_can_customize_functionalities`, `_compute_has_multicollo`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/delivery_sendcloud/Models]]

<!-- GENERATED:MODEL -->
