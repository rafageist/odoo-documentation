<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/equity_transaction_views.xml

- Module: [[docs/Enterprise Addons/equity/equity|equity]]
- Scope: Enterprise Addons
- Source file: `views/equity_transaction_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_equity_transaction_form`
- Name: equity.transaction.form
- Model: `equity.transaction`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `date`, `destination_class_id`, `equity_currency_id`, `expiration_date`, `expiration_diff`, `invalid_securities_error`, `notes`, `partner_id`, `securities`, `securities_type`, and 7 more
- Buttons: `action_transaction_seller_send`, `action_transaction_subscriber_send`, `equity.action_equity_valuation_form`
- XPath or positional patches: 0

### `view_equity_transaction_kanban`
- Name: equity.transaction.kanban
- Model: `equity.transaction`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `date`, `destination_class_id`, `equity_currency_id`, `securities`, `security_class_id`, `seller_name`, `subscriber_name`, `transaction_type`, `transfer_amount`
- XPath or positional patches: 0

### `view_equity_transaction_list`
- Name: equity.transaction.list
- Model: `equity.transaction`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `attachment_number`, `date`, `equity_currency_id`, `partner_id`, `securities`, `security_class_id`, `security_price`, `seller_id`, `subscriber_id`, `transaction_type`, and 1 more
- XPath or positional patches: 0

### `view_equity_transaction_search`
- Name: equity.transaction.search
- Model: `equity.transaction`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `partner_id`, `security_class_id`, `seller_id`, `subscriber_id`
- XPath or positional patches: 0

## Actions

- `action_equity_transaction`: `act_window` Transactions

## Navigation

- **Parent:** [[docs/Enterprise Addons/equity/Views]]

<!-- GENERATED:VIEWFILE -->
