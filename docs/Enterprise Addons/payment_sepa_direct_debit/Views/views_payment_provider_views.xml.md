<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/payment_provider_views.xml

- Module: [[docs/Enterprise Addons/payment_sepa_direct_debit/payment_sepa_direct_debit|payment_sepa_direct_debit]]
- Scope: Enterprise Addons
- Source file: `views/payment_provider_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `payment_provider_form_inherit_account_payment`
- Name: Sepa Provider Form 2
- Model: `payment.provider`
- Type: inferred from arch
- Inherits: `account_payment.payment_provider_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `journal_id`
- XPath or positional patches: 0

### `payment_provider_form_inherit_payment_custom`
- Name: Sepa Provider Form
- Model: `payment.provider`
- Type: inferred from arch
- Inherits: `payment_custom.payment_provider_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `allow_tokenization`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/payment_sepa_direct_debit/Views]]

<!-- GENERATED:VIEWFILE -->
