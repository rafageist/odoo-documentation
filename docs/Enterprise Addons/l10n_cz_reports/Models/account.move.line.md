<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.move.line

- Module: [[docs/Enterprise Addons/l10n_cz_reports/l10n_cz_reports|l10n_cz_reports]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_move_line.py`
- Python classes: `AccountMoveLine`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `is_reverse_charge`: `Boolean` (compute `_compute_is_reverse_charge`)
- `l10n_cz_supplies_code`: `Selection` (compute `_compute_l10n_cz_supplies_code`, store `True`)
- `l10n_cz_transaction_code`: `Selection` (compute `_compute_transaction_code`, store `True`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_is_reverse_charge`, `_compute_l10n_cz_supplies_code`, `_compute_transaction_code`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_cz_reports/Models]]

<!-- GENERATED:MODEL -->
