<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.partner

- Module: [[docs/Community Addons/account_peppol/account_peppol|account_peppol]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_partner.py`
- Python classes: `ResPartner`

## Field footprint

- Detected fields: 5
- Field types: `Json` x 2, `Selection` x 3
- Relation fields: 0

## Sample fields

- `available_peppol_edi_formats`: `Json` (compute `_compute_available_peppol_edi_formats`)
- `available_peppol_sending_methods`: `Json` (compute `_compute_available_peppol_sending_methods`)
- `invoice_sending_method`: `Selection`
- `peppol_eas`: `Selection`
- `peppol_verification_state`: `Selection`

## Method hints

- Detected methods: 12
- Action methods: none
- Compute methods: `_compute_available_peppol_eas`, `_compute_available_peppol_edi_formats`, `_compute_available_peppol_sending_methods`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/account_peppol/Models]]

<!-- GENERATED:MODEL -->
