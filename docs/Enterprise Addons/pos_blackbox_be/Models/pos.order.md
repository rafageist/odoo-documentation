<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# pos.order

- Module: [[docs/Enterprise Addons/pos_blackbox_be/pos_blackbox_be|pos_blackbox_be]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/pos_order.py`
- Python classes: `PosOrder`

## Field footprint

- Detected fields: 15
- Field types: `Boolean` x 1, `Char` x 9, `Datetime` x 1, `Monetary` x 4
- Relation fields: 0

## Sample fields

- `blackbox_date`: `Char` (comodel `Fiscal Data Module date`)
- `blackbox_order_sequence`: `Char` (comodel `Blackbox order sequence`)
- `blackbox_pos_receipt_time`: `Datetime` (comodel `Receipt time`, compute `_compute_blackbox_pos_receipt_time`)
- `blackbox_signature`: `Char` (comodel `Electronic signature`)
- `blackbox_tax_category_a`: `Monetary`
- `blackbox_tax_category_b`: `Monetary`
- `blackbox_tax_category_c`: `Monetary`
- `blackbox_tax_category_d`: `Monetary`
- `blackbox_ticket_counters`: `Char` (comodel `Fiscal Data Module ticket counters`)
- `blackbox_time`: `Char` (comodel `Fiscal Data Module time`)
- `blackbox_unique_fdm_production_number`: `Char` (comodel `Fiscal Data Module ID`)
- `blackbox_vsc_identification_number`: `Char` (comodel `VAT Signing Card ID`)
- `is_clock`: `Boolean` (comodel `Is clock in/out`, compute `_compute_is_clock`)
- `plu_hash`: `Char`
- `pos_version`: `Char`

## Method hints

- Detected methods: 12
- Action methods: `action_pos_order_cancel`
- Compute methods: `_compute_blackbox_pos_receipt_time`, `_compute_is_clock`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_blackbox_be/Models]]

<!-- GENERATED:MODEL -->
