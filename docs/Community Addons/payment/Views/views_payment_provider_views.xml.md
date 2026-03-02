<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/payment_provider_views.xml

- Module: [[docs/Community Addons/payment/payment|payment]]
- Scope: Community Addons
- Source file: `views/payment_provider_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `payment_provider_search`
- Name: payment.provider.search
- Model: `payment.provider`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `payment_method_ids`
- XPath or positional patches: 0

### `payment_provider_kanban`
- Name: payment.provider.kanban
- Model: `payment.provider`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `company_id`, `image_128`, `is_published`, `module_id`, `module_state`, `module_to_buy`, `name`, `state`
- Buttons: `button_immediate_install`
- XPath or positional patches: 0

### `payment_provider_list`
- Name: payment.provider.list
- Model: `payment.provider`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `available_country_ids`, `code`, `company_id`, `name`, `sequence`, `state`
- XPath or positional patches: 0

### `payment_provider_form`
- Name: payment.provider.form
- Model: `payment.provider`
- Type: inferred from arch
- Root tag: `form`
- Field references: 18
- Sample fields: `allow_express_checkout`, `allow_tokenization`, `auth_msg`, `available_country_ids`, `available_currency_ids`, `cancel_msg`, `capture_manually`, `code`, `company_id`, `done_msg`, and 8 more
- Buttons: `action_toggle_is_published`, `button_immediate_install`
- XPath or positional patches: 0

## Actions

- `action_payment_provider`: `act_window` Payment Providers

## Navigation

- **Parent:** [[docs/Community Addons/payment/Views]]

<!-- GENERATED:VIEWFILE -->
