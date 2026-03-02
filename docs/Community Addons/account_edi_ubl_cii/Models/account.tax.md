<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.tax

- Module: [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/account_tax.py`
- Python classes: `AccountTax`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `ubl_cii_requires_exemption_reason`: `Boolean` (compute `_compute_ubl_cii_requires_exemption_reason`)
- `ubl_cii_tax_category_code`: `Selection`
- `ubl_cii_tax_exemption_reason_code`: `Selection`

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_ubl_cii_requires_exemption_reason`
- Onchange methods: `_onchange_ubl_cii_tax_category_code`

## Navigation

- **Parent:** [[docs/Community Addons/account_edi_ubl_cii/Models]]

<!-- GENERATED:MODEL -->
