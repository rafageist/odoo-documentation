<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# payment.provider

- Module: [[docs/Community Addons/payment_stripe/payment_stripe|payment_stripe]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/payment_provider.py`
- Python classes: `PaymentProvider`

## Field footprint

- Detected fields: 4
- Field types: `Char` x 3, `Selection` x 1
- Relation fields: 0

## Sample fields

- `code`: `Selection`
- `stripe_publishable_key`: `Char`
- `stripe_secret_key`: `Char`
- `stripe_webhook_secret`: `Char`

## Method hints

- Detected methods: 23
- Action methods: `action_start_onboarding`, `action_stripe_create_webhook`, `action_stripe_verify_apple_pay_domain`
- Compute methods: `_compute_feature_support_fields`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/payment_stripe/Models]]

<!-- GENERATED:MODEL -->
