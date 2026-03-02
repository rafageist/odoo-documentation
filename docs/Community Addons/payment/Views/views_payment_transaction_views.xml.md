<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/payment_transaction_views.xml

- Module: [[docs/Community Addons/payment/payment|payment]]
- Scope: Community Addons
- Source file: `views/payment_transaction_views.xml`
- Views: 6
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `payment_transaction_pivot`
- Name: payment.transaction.pivot
- Model: `payment.transaction`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `amount`, `create_date`, `state`
- XPath or positional patches: 0

### `payment_transaction_graph`
- Name: payment.transaction.graph
- Model: `payment.transaction`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `create_date`, `state`
- XPath or positional patches: 0

### `payment_transaction_search`
- Name: payment.transaction.search
- Model: `payment.transaction`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `partner_id`, `partner_name`, `provider_id`, `reference`
- XPath or positional patches: 0

### `payment_transaction_kanban`
- Name: payment.transaction.kanban
- Model: `payment.transaction`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `amount`, `currency_id`, `partner_name`, `reference`
- XPath or positional patches: 0

### `payment_transaction_list`
- Name: payment.transaction.list
- Model: `payment.transaction`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `amount`, `company_id`, `create_date`, `currency_id`, `is_live`, `partner_id`, `partner_name`, `payment_method_id`, `provider_id`, `reference`, and 1 more
- XPath or positional patches: 0

### `payment_transaction_form`
- Name: payment.transaction.form
- Model: `payment.transaction`
- Type: inferred from arch
- Root tag: `form`
- Field references: 27
- Sample fields: `amount`, `child_transaction_ids`, `company_id`, `create_date`, `currency_id`, `is_live`, `is_post_processed`, `last_state_change`, `partner_address`, `partner_city`, and 17 more
- Buttons: `action_capture`, `action_view_refunds`, `action_void`
- XPath or positional patches: 0

## Actions

- `action_payment_transaction_linked_to_token`: `act_window` Payment Transactions Linked To Token
- `action_payment_transaction`: `act_window` Payment Transactions

## Navigation

- **Parent:** [[docs/Community Addons/payment/Views]]

<!-- GENERATED:VIEWFILE -->
