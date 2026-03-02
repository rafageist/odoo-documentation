<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_batch_payment_views.xml

- Module: [[docs/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]]
- Scope: Enterprise Addons
- Source file: `views/account_batch_payment_views.xml`
- Views: 4
- Actions: 3
- Menus: 2
- Rules: 0

## View records

### `view_account_move_kanban`
- Name: account.batch.payment.move.kanban
- Model: `account.batch.payment`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `activity_ids`, `amount`, `currency_id`, `date`, `name`, `state`
- XPath or positional patches: 0

### `view_batch_payment_tree`
- Name: account.batch.payment.list
- Model: `account.batch.payment`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `activity_ids`, `amount`, `currency_id`, `date`, `journal_id`, `name`, `state`
- XPath or positional patches: 0

### `view_batch_payment_search`
- Name: account.batch.payment.search
- Model: `account.batch.payment`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `amount`, `journal_id`, `name`
- XPath or positional patches: 0

### `view_batch_payment_form`
- Name: account.batch.payment.form
- Model: `account.batch.payment`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `amount_signed`, `available_payment_method_ids`, `batch_type`, `currency_id`, `date`, `file_generation_enabled`, `id`, `invalid_sct_partners_ids`, `journal_id`, `memo`, and 7 more
- Buttons: `print_batch_payment`, `validate_batch_button`
- XPath or positional patches: 0

## Actions

- `action_batch_payment_out`: `act_window` Vendor Batch Payments
- `action_batch_payment_in`: `act_window` Customer Batch Payments
- `action_account_create_batch_payment`: `server` Create batch payment

## Menus

- `menu_batch_payment_purchases`: Batch Payments
- `menu_batch_payment_sales`: Batch Payments

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_batch_payment/Views]]

<!-- GENERATED:VIEWFILE -->
