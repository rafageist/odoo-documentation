<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sale.temporal.recurrence

- Module: [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/sale_order_recurrence.py`
- Python classes: `SaleTemporalRecurrence`
- Description: Sale temporal Recurrence

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 2, `Char` x 2, `Float` x 2, `Integer` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `active`: `Boolean`
- `displayed_unit`: `Selection` (compute `_compute_displayed_unit`)
- `duration`: `Integer`
- `duration_display`: `Char` (compute `_compute_duration_display`)
- `name`: `Char`
- `overnight`: `Boolean`
- `pickup_time`: `Float`
- `return_time`: `Float`
- `unit`: `Selection`

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_displayed_unit`, `_compute_duration_display`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_renting/Models]]

<!-- GENERATED:MODEL -->
