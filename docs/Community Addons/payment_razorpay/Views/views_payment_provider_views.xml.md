---
tags: [odoo, community, generated, views]
---

# views/payment_provider_views.xml

- Module: [[docs/Community Addons/payment_razorpay/payment_razorpay|payment_razorpay]]
- Scope: Community Addons
- Source file: `views/payment_provider_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `payment_provider_form_razorpay`
- Name: Razorpay Provider Form
- Model: `payment.provider`
- Type: inferred from arch
- Inherits: `payment.payment_provider_form`
- Root tag: `group`
- Field references: 5
- Sample fields: `allow_tokenization`, `razorpay_account_id`, `razorpay_key_id`, `razorpay_key_secret`, `razorpay_webhook_secret`
- Buttons: `action_razorpay_create_webhook`, `action_reset_credentials`, `action_start_onboarding`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Community Addons/payment_razorpay/Views]]

