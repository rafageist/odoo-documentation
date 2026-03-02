<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# stock.picking

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/l10n_ke_edi_oscu_stock|l10n_ke_edi_oscu_stock]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/stock_picking.py`
- Python classes: `StockPicking`

## Field footprint

- Detected fields: 5
- Field types: `Integer` x 1, `Json` x 2, `Selection` x 2
- Relation fields: 0

## Sample fields

- `l10n_ke_error_msg`: `Json`
- `l10n_ke_oscu_flow_type_code`: `Selection` (related `move_ids.l10n_ke_oscu_flow_type_code`)
- `l10n_ke_oscu_sar_number`: `Integer` (related `move_ids.l10n_ke_oscu_sar_number`)
- `l10n_ke_state`: `Selection` (compute `_compute_l10n_ke_state`)
- `l10n_ke_validation_msg`: `Json` (compute `_compute_l10n_ke_validation_msg`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_l10n_ke_state`, `_compute_l10n_ke_validation_msg`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/Models]]

<!-- GENERATED:MODEL -->
