<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# purchase.order

- Module: [[docs/Enterprise Addons/partner_commission/partner_commission|partner_commission]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/purchase_order.py`
- Python classes: `PurchaseOrder`

## Field footprint

- Detected fields: 2
- Field types: `Integer` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `invoice_commission_count`: `Integer` (comodel `Source Invoices`, compute `_compute_source_invoice_count`)
- `purchase_type`: `Selection`

## Method hints

- Detected methods: 3
- Action methods: `action_view_customer_invoices`
- Compute methods: `_compute_source_invoice_count`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/partner_commission/Models]]

<!-- GENERATED:MODEL -->
