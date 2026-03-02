<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.picking.type

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/stock_picking.py`
- Python classes: `StockPickingType`

## Field footprint

- Detected fields: 16
- Field types: `Boolean` x 7, `Integer` x 5, `Selection` x 4
- Relation fields: 0

## Sample fields

- `auto_print_done_mrp_lot`: `Boolean` (comodel `Auto Print Produced Lot Label`)
- `auto_print_done_mrp_product_labels`: `Boolean` (comodel `Auto Print Produced Product Labels`)
- `auto_print_done_production_order`: `Boolean` (comodel `Auto Print Done Production Order`)
- `auto_print_generated_mrp_lot`: `Boolean` (comodel `Auto Print Generated Lot/SN Label`)
- `auto_print_mrp_reception_report`: `Boolean` (comodel `Auto Print Allocation Report`)
- `auto_print_mrp_reception_report_labels`: `Boolean` (comodel `Auto Print Allocation Report Labels`)
- `code`: `Selection`
- `count_mo_in_progress`: `Integer` (compute `_get_mo_count`)
- `count_mo_late`: `Integer` (compute `_get_mo_count`)
- `count_mo_to_close`: `Integer` (compute `_get_mo_count`)
- `count_mo_todo`: `Integer` (compute `_get_mo_count`)
- `count_mo_waiting`: `Integer` (compute `_get_mo_count`)
- `done_mrp_lot_label_to_print`: `Selection`
- `generated_mrp_lot_label_to_print`: `Selection`
- `mrp_product_label_to_print`: `Selection`
- `use_create_components_lots`: `Boolean`

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_use_create_lots`, `_compute_use_existing_lots`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Models]]

<!-- GENERATED:MODEL -->
