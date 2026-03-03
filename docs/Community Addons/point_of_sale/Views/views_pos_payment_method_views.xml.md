---
tags: [odoo, community, generated, views]
---

# views/pos_payment_method_views.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/pos_payment_method_views.xml`
- Views: 3
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `pos_payment_method_view_search`
- Name: pos.payment.search.view
- Model: `pos.payment.method`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `receivable_account_id`
- XPath or positional patches: 0

### `pos_payment_method_view_tree`
- Name: pos.payment.method.list
- Model: `pos.payment.method`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `company_id`, `config_ids`, `journal_id`, `name`, `outstanding_account_id`, `receivable_account_id`, `sequence`, `split_transactions`, `type`
- XPath or positional patches: 0

### `pos_payment_method_view_form`
- Name: pos.payment.method.form
- Model: `pos.payment.method`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `active`, `company_id`, `config_ids`, `default_pos_receivable_account_name`, `hide_qr_code_method`, `hide_use_payment_terminal`, `image`, `journal_id`, `name`, `outstanding_account_id`, and 6 more
- XPath or positional patches: 0

## Actions

- `action_payment_methods_tree`: `act_window` Payments Methods
- `action_pos_payment_method_form`: `act_window` Payment Methods

## Menus

- `menu_pos_payment_method`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

