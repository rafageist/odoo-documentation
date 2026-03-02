<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# stock.move

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/l10n_ke_edi_oscu_stock|l10n_ke_edi_oscu_stock]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/stock_move.py`
- Python classes: `StockMove`

## Field footprint

- Detected fields: 4
- Field types: `Binary` x 1, `Char` x 1, `Integer` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `country_code`: `Char` (related `company_id.account_fiscal_country_id.code`)
- `l10n_ke_oscu_attachment_file`: `Binary`
- `l10n_ke_oscu_flow_type_code`: `Selection` (compute `_compute_l10n_ke_oscu_flow_type_code`, store `True`)
- `l10n_ke_oscu_sar_number`: `Integer`

## Method hints

- Detected methods: 8
- Action methods: `action_l10n_ke_oscu_process_moves`
- Compute methods: `_compute_l10n_ke_oscu_flow_type_code`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/Models]]

<!-- GENERATED:MODEL -->
