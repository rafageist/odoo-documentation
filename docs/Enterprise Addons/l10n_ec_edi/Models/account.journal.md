<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.journal

- Module: [[docs/Enterprise Addons/l10n_ec_edi/l10n_ec_edi|l10n_ec_edi]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_journal.py`
- Python classes: `AccountJournal`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_ec_is_purchase_liquidation`: `Boolean`
- `l10n_ec_withhold_type`: `Selection`

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_compatible_edi_ids`, `_compute_edi_format_ids`, `_compute_l10n_ec_require_emission`
- Onchange methods: `_onchange_type_is_purchase_liquidation`, `_onchange_withhold_type`

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ec_edi/Models]]

<!-- GENERATED:MODEL -->
