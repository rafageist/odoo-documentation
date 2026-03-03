<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# base.document.layout

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `wizard/base_document_layout.py`
- Python classes: `BaseDocumentLayout`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 2, `Char` x 2
- Relation fields: 0

## Sample fields

- `account_number`: `Char` (compute `_compute_account_number`)
- `from_invoice`: `Boolean`
- `qr_code`: `Boolean` (related `company_id.qr_code`)
- `vat`: `Char` (related `company_id.vat`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_account_number`, `_compute_preview`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/account/Models]]

<!-- GENERATED:MODEL -->
