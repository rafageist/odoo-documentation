<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mailing.mailing

- Module: [[docs/Community Addons/mass_mailing_sale/mass_mailing_sale|mass_mailing_sale]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/mailing_mailing.py`
- Python classes: `MailingMailing`

## Field footprint

- Detected fields: 2
- Field types: `Integer` x 2
- Relation fields: 0

## Sample fields

- `sale_invoiced_amount`: `Integer` (comodel `Invoiced Amount`, compute `_compute_sale_invoiced_amount`)
- `sale_quotation_count`: `Integer` (comodel `Quotation Count`, compute `_compute_sale_quotation_count`)

## Method hints

- Detected methods: 5
- Action methods: `action_redirect_to_invoiced`, `action_redirect_to_quotations`
- Compute methods: `_compute_sale_invoiced_amount`, `_compute_sale_quotation_count`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing_sale/Models]]

<!-- GENERATED:MODEL -->
