<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.company

- Module: [[docs/Enterprise Addons/account_iso20022/account_iso20022|account_iso20022]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 4
- Field types: `Char` x 4
- Relation fields: 0

## Sample fields

- `iso20022_initiating_party_name`: `Char` (comodel `Your Company Name`)
- `iso20022_lei`: `Char` (related `partner_id.iso20022_lei`)
- `iso20022_orgid_id`: `Char` (comodel `Identification`, compute `_compute_iso20022_orgid`, store `True`)
- `iso20022_orgid_issr`: `Char` (comodel `Issuer`, compute `_compute_iso20022_orgid`, store `True`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_iso20022_orgid`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_iso20022/Models]]

<!-- GENERATED:MODEL -->
