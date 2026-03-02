<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.move.line

- Module: [[docs/Community Addons/l10n_gr_edi/l10n_gr_edi|l10n_gr_edi]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/account_move_line.py`
- Python classes: `AccountMoveLine`

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 1, `Char` x 3, `Selection` x 5
- Relation fields: 0

## Sample fields

- `l10n_gr_edi_available_cls_category`: `Char` (compute `_compute_l10n_gr_edi_available_cls_category`)
- `l10n_gr_edi_available_cls_type`: `Char` (compute `_compute_l10n_gr_edi_available_cls_type`)
- `l10n_gr_edi_available_cls_vat`: `Char` (compute `_compute_l10n_gr_edi_available_cls_type`)
- `l10n_gr_edi_cls_category`: `Selection` (compute `_compute_l10n_gr_edi_cls_category`, store `True`)
- `l10n_gr_edi_cls_type`: `Selection` (compute `_compute_l10n_gr_edi_cls_type`, store `True`)
- `l10n_gr_edi_cls_vat`: `Selection` (compute `_compute_l10n_gr_edi_cls_vat`, store `True`)
- `l10n_gr_edi_detail_type`: `Selection` (compute `_compute_l10n_gr_edi_detail_type`, store `True`)
- `l10n_gr_edi_need_exemption_category`: `Boolean` (compute `_compute_l10n_gr_edi_need_exemption_category`)
- `l10n_gr_edi_tax_exemption_category`: `Selection` (compute `_compute_l10n_gr_edi_tax_exemption_category`, store `True`)

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_l10n_gr_edi_available_cls_category`, `_compute_l10n_gr_edi_available_cls_type`, `_compute_l10n_gr_edi_cls_category`, `_compute_l10n_gr_edi_cls_type`, `_compute_l10n_gr_edi_cls_vat`, `_compute_l10n_gr_edi_detail_type`, `_compute_l10n_gr_edi_need_exemption_category`, `_compute_l10n_gr_edi_tax_exemption_category`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/l10n_gr_edi/Models]]

<!-- GENERATED:MODEL -->
