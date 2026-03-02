<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# payment.link.wizard

- Module: [[docs/Community Addons/account_payment/account_payment|account_payment]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `wizards/payment_link_wizard.py`
- Python classes: `PaymentLinkWizard`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 2, `Char` x 1, `Date` x 1, `Html` x 1, `Json` x 1, `Monetary` x 1
- Relation fields: 0

## Sample fields

- `discount_date`: `Date`
- `display_open_installments`: `Boolean` (compute `_compute_display_open_installments`)
- `epd_info`: `Char` (compute `_compute_epd_info`)
- `has_eligible_epd`: `Boolean`
- `invoice_amount_due`: `Monetary` (compute `_compute_invoice_amount_due`)
- `open_installments`: `Json`
- `open_installments_preview`: `Html` (compute `_compute_open_installments_preview`)

## Method hints

- Detected methods: 9
- Action methods: none
- Compute methods: `_compute_display_open_installments`, `_compute_epd_info`, `_compute_invoice_amount_due`, `_compute_open_installments_preview`, `_compute_warning_message`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/account_payment/Models]]

<!-- GENERATED:MODEL -->
