<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.move

- Module: [[docs/Community Addons/l10n_cl/l10n_cl|l10n_cl]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/account_move.py`
- Python classes: `AccountMove`

## Field footprint

- Detected fields: 2
- Field types: `Char` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_latam_internal_type`: `Selection` (related `l10n_latam_document_type_id.internal_type`)
- `partner_id_vat`: `Char` (related `partner_id.vat`)

## Method hints

- Detected methods: 16
- Action methods: none
- Compute methods: `_compute_tax_totals`
- Onchange methods: `_l10n_cl_onchange_journal`

## Navigation

- **Parent:** [[docs/Community Addons/l10n_cl/Models]]

<!-- GENERATED:MODEL -->
