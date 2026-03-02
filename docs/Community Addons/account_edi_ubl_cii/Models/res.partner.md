<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.partner

- Module: [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_partner.py`
- Python classes: `ResPartner`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 2, `Char` x 1, `Json` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `available_peppol_eas`: `Json` (compute `_compute_available_peppol_eas`)
- `invoice_edi_format`: `Selection`
- `is_peppol_edi_format`: `Boolean` (compute `_compute_is_peppol_edi_format`)
- `is_ubl_format`: `Boolean` (compute `_compute_is_ubl_format`)
- `peppol_eas`: `Selection` (compute `_compute_peppol_eas`, store `True`)
- `peppol_endpoint`: `Char` (compute `_compute_peppol_endpoint`, store `True`)

## Method hints

- Detected methods: 16
- Action methods: none
- Compute methods: `_compute_available_peppol_eas`, `_compute_is_peppol_edi_format`, `_compute_is_ubl_format`, `_compute_peppol_eas`, `_compute_peppol_endpoint`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/account_edi_ubl_cii/Models]]

<!-- GENERATED:MODEL -->
