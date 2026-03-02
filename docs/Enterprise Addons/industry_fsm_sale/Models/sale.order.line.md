<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sale.order.line

- Module: [[docs/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/sale_order.py`
- Python classes: `SaleOrderLine`

## Field footprint

- Detected fields: 3
- Field types: `Float` x 1, `Monetary` x 2
- Relation fields: 0

## Sample fields

- `delivered_price_subtotal`: `Monetary` (compute `_compute_delivered_amount`)
- `delivered_price_tax`: `Float` (compute `_compute_delivered_amount`)
- `delivered_price_total`: `Monetary` (compute `_compute_delivered_amount`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_delivered_amount`, `_compute_invoice_status`, `_compute_qty_to_invoice`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_sale/Models]]

<!-- GENERATED:MODEL -->
