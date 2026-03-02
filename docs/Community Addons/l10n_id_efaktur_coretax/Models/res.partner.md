<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.partner

- Module: [[docs/Community Addons/l10n_id_efaktur_coretax/l10n_id_efaktur_coretax|l10n_id_efaktur_coretax]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_partner.py`
- Python classes: `Partner`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Char` x 3, `Selection` x 2
- Relation fields: 0

## Sample fields

- `l10n_id_buyer_document_number`: `Char`
- `l10n_id_buyer_document_type`: `Selection`
- `l10n_id_kode_transaksi`: `Selection`
- `l10n_id_nik`: `Char`
- `l10n_id_pkp`: `Boolean` (compute `_compute_l10n_id_pkp`, store `True`)
- `l10n_id_tku`: `Char`

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_l10n_id_pkp`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/l10n_id_efaktur_coretax/Models]]

<!-- GENERATED:MODEL -->
