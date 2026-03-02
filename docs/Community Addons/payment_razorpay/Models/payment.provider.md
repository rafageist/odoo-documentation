<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# payment.provider

- Module: [[docs/Community Addons/payment_razorpay/payment_razorpay|payment_razorpay]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/payment_provider.py`
- Python classes: `PaymentProvider`

## Field footprint

- Detected fields: 9
- Field types: `Char` x 7, `Datetime` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `code`: `Selection`
- `razorpay_access_token`: `Char`
- `razorpay_access_token_expiry`: `Datetime`
- `razorpay_account_id`: `Char`
- `razorpay_key_id`: `Char`
- `razorpay_key_secret`: `Char`
- `razorpay_public_token`: `Char`
- `razorpay_refresh_token`: `Char`
- `razorpay_webhook_secret`: `Char`

## Method hints

- Detected methods: 15
- Action methods: `action_razorpay_create_webhook`, `action_start_onboarding`
- Compute methods: `_compute_feature_support_fields`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/payment_razorpay/Models]]

<!-- GENERATED:MODEL -->
