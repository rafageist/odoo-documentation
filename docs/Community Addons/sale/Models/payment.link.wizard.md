<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# payment.link.wizard

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `wizard/payment_link_wizard.py`
- Python classes: `PaymentLinkWizard`
- Description: Generate Sales Payment Link

## Field footprint

- Detected fields: 3
- Field types: `Char` x 1, `Monetary` x 2
- Relation fields: 0

## Sample fields

- `amount_paid`: `Monetary`
- `confirmation_message`: `Char` (compute `_compute_confirmation_message`)
- `prepayment_amount`: `Monetary`

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_confirmation_message`, `_compute_warning_message`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/sale/Models]]

<!-- GENERATED:MODEL -->
