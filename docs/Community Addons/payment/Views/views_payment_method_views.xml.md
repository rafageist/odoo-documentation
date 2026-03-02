<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/payment_method_views.xml

- Module: [[docs/Community Addons/payment/payment|payment]]
- Scope: Community Addons
- Source file: `views/payment_method_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `payment_method_search`
- Name: payment.method.search
- Model: `payment.method`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `payment_method_kanban`
- Name: payment.method.kanban
- Model: `payment.method`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `image`, `name`
- XPath or positional patches: 0

### `payment_method_tree`
- Name: payment.method.list
- Model: `payment.method`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `active`, `name`, `sequence`
- XPath or positional patches: 0

### `payment_method_form`
- Name: payment.method.form
- Model: `payment.method`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `active`, `brand_ids`, `code`, `image`, `is_primary`, `name`, `primary_payment_method_id`, `provider_ids`, `state`, `support_express_checkout`, and 5 more
- XPath or positional patches: 0

## Actions

- `action_payment_method`: `act_window` Payment Methods

## Navigation

- **Parent:** [[docs/Community Addons/payment/Views]]

<!-- GENERATED:VIEWFILE -->
