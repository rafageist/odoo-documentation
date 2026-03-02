<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.move

- Module: [[docs/Community Addons/l10n_sa/l10n_sa|l10n_sa]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/account_move.py`
- Python classes: `AccountMove`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 1, `Char` x 1, `Datetime` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_sa_confirmation_datetime`: `Datetime`
- `l10n_sa_qr_code_str`: `Char` (compute `_compute_qr_code_str`)
- `l10n_sa_reason`: `Selection`
- `l10n_sa_show_reason`: `Boolean` (compute `_compute_show_l10n_sa_reason`)

## Method hints

- Detected methods: 12
- Action methods: none
- Compute methods: `_compute_qr_code_str`, `_compute_show_delivery_date`, `_compute_show_l10n_sa_reason`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/l10n_sa/Models]]

<!-- GENERATED:MODEL -->
