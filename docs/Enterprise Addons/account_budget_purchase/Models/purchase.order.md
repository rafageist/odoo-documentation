<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# purchase.order

- Module: [[docs/Enterprise Addons/account_budget_purchase/account_budget_purchase|account_budget_purchase]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/purchase_order.py`
- Python classes: `PurchaseOrder`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 2
- Relation fields: 0

## Sample fields

- `is_above_budget`: `Boolean` (comodel `Is Above Budget`, compute `_compute_above_budget`)
- `is_analytic`: `Boolean` (comodel `Is Analytic`, compute `_compute_is_analytic`)

## Method hints

- Detected methods: 3
- Action methods: `action_budget`
- Compute methods: `_compute_above_budget`, `_compute_is_analytic`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_budget_purchase/Models]]

<!-- GENERATED:MODEL -->
