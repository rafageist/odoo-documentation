<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.picking

- Module: [[docs/Community Addons/l10n_it_stock_ddt/l10n_it_stock_ddt|l10n_it_stock_ddt]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/stock_picking.py`
- Python classes: `StockPicking`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Char` x 2, `Integer` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `l10n_it_ddt_number`: `Char` (comodel `DDT Number`)
- `l10n_it_parcels`: `Integer`
- `l10n_it_show_print_ddt_button`: `Boolean` (compute `_compute_l10n_it_show_print_ddt_button`)
- `l10n_it_transport_method`: `Selection`
- `l10n_it_transport_method_details`: `Char` (comodel `Transport Note`)
- `l10n_it_transport_reason`: `Selection`

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_l10n_it_show_print_ddt_button`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/l10n_it_stock_ddt/Models]]

<!-- GENERATED:MODEL -->
