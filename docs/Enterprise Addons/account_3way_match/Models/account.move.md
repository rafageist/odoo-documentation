<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.move

- Module: [[docs/Enterprise Addons/account_3way_match/account_3way_match|account_3way_match]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_invoice.py`
- Python classes: `AccountMove`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `force_release_to_pay`: `Boolean`
- `release_to_pay`: `Selection` (compute `_compute_release_to_pay`, store `True`)
- `release_to_pay_manual`: `Selection` (compute `_compute_release_to_pay_manual`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_release_to_pay`, `_compute_release_to_pay_manual`
- Onchange methods: `_onchange_release_to_pay_manual`

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_3way_match/Models]]

<!-- GENERATED:MODEL -->
