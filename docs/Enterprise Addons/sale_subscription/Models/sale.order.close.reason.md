<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sale.order.close.reason

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/sale_order_close_reason.py`
- Python classes: `SaleOrderCloseReason`
- Description: Subscription Close Reason

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 3, `Char` x 3, `Html` x 1, `Integer` x 1
- Relation fields: 0

## Sample fields

- `empty_retention_message`: `Boolean` (compute `_compute_empty_retention_message`)
- `is_protected`: `Boolean`
- `name`: `Char` (comodel `Reason`)
- `retention_button_link`: `Char` (comodel `Button Link`)
- `retention_button_text`: `Char` (comodel `Button Text`)
- `retention_message`: `Html` (comodel `Message`)
- `sequence`: `Integer`
- `visible_in_portal`: `Boolean`

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_empty_retention_message`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Models]]

<!-- GENERATED:MODEL -->
