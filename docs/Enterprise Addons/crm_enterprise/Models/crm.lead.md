<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# crm.lead

- Module: [[docs/Enterprise Addons/crm_enterprise/crm_enterprise|crm_enterprise]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/crm_lead.py`
- Python classes: `CrmLead`

## Field footprint

- Detected fields: 2
- Field types: `Float` x 2
- Relation fields: 0

## Sample fields

- `days_exceeding_closing`: `Float` (comodel `Exceeded Closing Days`, compute `_compute_days_exceeding_closing`, store `True`)
- `days_to_convert`: `Float` (comodel `Days To Convert`, compute `_compute_days_to_convert`, store `True`)

## Method hints

- Detected methods: 3
- Action methods: `action_ocr_business_cards`
- Compute methods: `_compute_days_exceeding_closing`, `_compute_days_to_convert`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/crm_enterprise/Models]]

<!-- GENERATED:MODEL -->
