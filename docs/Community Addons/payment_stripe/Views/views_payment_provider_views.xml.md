---
tags: [odoo, community, generated, views]
---

# views/payment_provider_views.xml

- Module: [[docs/Community Addons/payment_stripe/payment_stripe|payment_stripe]]
- Scope: Community Addons
- Source file: `views/payment_provider_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `payment_provider_form`
- Name: Stripe Provider Form
- Model: `payment.provider`
- Type: inferred from arch
- Inherits: `payment.payment_provider_form`
- Root tag: `group`
- Field references: 4
- Sample fields: `allow_express_checkout`, `stripe_publishable_key`, `stripe_secret_key`, `stripe_webhook_secret`
- Buttons: `action_start_onboarding`, `action_stripe_create_webhook`, `action_stripe_verify_apple_pay_domain`
- XPath or positional patches: 2

## Actions

- `action_payment_provider_onboarding`: `act_window` Payment Providers

## Navigation

- **Parent:** [[docs/Community Addons/payment_stripe/Views]]

