<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.move

- Module: [[docs/Enterprise Addons/l10n_pe_edi/l10n_pe_edi|l10n_pe_edi]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_move.py`
- Python classes: `AccountMove`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 1, `Char` x 3, `Selection` x 4
- Relation fields: 0

## Sample fields

- `l10n_pe_edi_cancel_cdr_number`: `Char`
- `l10n_pe_edi_cancel_reason`: `Char`
- `l10n_pe_edi_charge_reason`: `Selection`
- `l10n_pe_edi_is_required`: `Boolean` (compute `_compute_l10n_pe_edi_is_required`)
- `l10n_pe_edi_legend`: `Selection`
- `l10n_pe_edi_legend_value`: `Char` (compute `_compute_l10n_pe_edi_legend_value`, store `True`)
- `l10n_pe_edi_operation_type`: `Selection` (compute `_compute_l10n_pe_edi_operation_type`, store `True`)
- `l10n_pe_edi_refund_reason`: `Selection`

## Method hints

- Detected methods: 15
- Action methods: none
- Compute methods: `_compute_l10n_latam_available_document_types`, `_compute_l10n_pe_edi_is_required`, `_compute_l10n_pe_edi_legend_value`, `_compute_l10n_pe_edi_operation_type`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_pe_edi/Models]]

<!-- GENERATED:MODEL -->
