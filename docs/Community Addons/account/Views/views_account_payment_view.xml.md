<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_payment_view.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/account_payment_view.xml`
- Views: 7
- Actions: 7
- Menus: 0
- Rules: 0

## View records

### `view_account_payment_graph`
- Name: account.payment.graph
- Model: `account.payment`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `amount`, `journal_id`, `payment_type`
- XPath or positional patches: 0

### `view_account_payment_form`
- Name: account.payment.form
- Model: `account.payment`
- Type: inferred from arch
- Root tag: `form`
- Field references: 32
- Sample fields: `amount`, `available_journal_ids`, `available_partner_bank_ids`, `available_payment_method_line_ids`, `company_id`, `country_code`, `currency_id`, `date`, `duplicate_payment_ids`, `id`, and 22 more
- Buttons: `action_cancel`, `action_draft`, `action_post`, `action_reject`, `action_validate`, `button_open_bills`, `button_open_invoices`, `button_open_journal_entry`, `button_open_statement_lines`, `button_request_cancel`, and 2 more
- XPath or positional patches: 0

### `view_account_payment_search`
- Name: account.payment.search
- Model: `account.payment`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `company_id`, `journal_id`, `name`, `partner_id`
- XPath or positional patches: 0

### `view_account_payment_kanban`
- Name: account.payment.kanban
- Model: `account.payment`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `activity_ids`, `amount`, `currency_id`, `date`, `journal_id`, `name`, `partner_id`, `state`
- XPath or positional patches: 0

### `view_account_various_payment_tree`
- Name: account.supplier.payment.list
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_tree`
- Root tag: `field`
- Field references: 1
- Sample fields: `partner_id`
- XPath or positional patches: 0

### `view_account_supplier_payment_tree`
- Name: account.supplier.payment.list
- Model: `account.payment`
- Type: inferred from arch
- Inherits: `account.view_account_payment_tree`
- Root tag: `field`
- Field references: 1
- Sample fields: `partner_id`
- XPath or positional patches: 0

### `view_account_payment_tree`
- Name: account.payment.list
- Model: `account.payment`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `activity_ids`, `amount_company_currency_signed`, `amount_signed`, `available_payment_method_line_ids`, `company_currency_id`, `company_id`, `currency_id`, `date`, `journal_id`, `name`, and 3 more
- Buttons: `action_post`
- XPath or positional patches: 0

## Actions

- `account_send_payment_receipt_by_email_action_multi`: `act_window` Send receipts by email
- `account_send_payment_receipt_by_email_action`: `act_window` Send receipt by email
- `action_account_confirm_payments`: `server` Post Payments
- `action_account_payments_transfer`: `act_window` Internal Transfers
- `action_account_payments_payable`: `act_window` Vendor Payments
- `action_account_payments`: `act_window` Customer Payments
- `action_account_all_payments`: `act_window` Payments

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
