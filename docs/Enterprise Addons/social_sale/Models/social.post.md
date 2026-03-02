<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.post

- Module: [[docs/Enterprise Addons/social_sale/social_sale|social_sale]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/social_post.py`
- Python classes: `SocialPost`

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

- **Parent:** [[docs/Enterprise Addons/social_sale/Models]]

<!-- GENERATED:MODEL -->
