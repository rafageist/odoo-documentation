<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# pos.payment.method

- Module: [[docs/Community Addons/pos_viva_com/pos_viva_com|pos_viva_com]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/pos_payment_method.py`
- Python classes: `PosPaymentMethod`

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 1, `Char` x 8, `Json` x 1
- Relation fields: 0

## Sample fields

- `viva_com_api_key`: `Char`
- `viva_com_bearer_token`: `Char`
- `viva_com_client_id`: `Char`
- `viva_com_client_secret`: `Char`
- `viva_com_latest_response`: `Json`
- `viva_com_merchant_id`: `Char`
- `viva_com_terminal_id`: `Char`
- `viva_com_test_mode`: `Boolean`
- `viva_com_webhook_endpoint`: `Char` (compute `_compute_viva_com_webhook_endpoint`)
- `viva_com_webhook_verification_key`: `Char`

## Method hints

- Detected methods: 19
- Action methods: none
- Compute methods: `_compute_viva_com_webhook_endpoint`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/pos_viva_com/Models]]

<!-- GENERATED:MODEL -->
