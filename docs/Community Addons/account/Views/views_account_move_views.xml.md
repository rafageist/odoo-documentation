<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 31
- Actions: 28
- Menus: 0
- Rules: 0

## View records

### `view_account_move_with_gaps_in_sequence_filter`
- Name: account.move.with.gaps.in.sequence.filter
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_account_bill_filter`
- Name: account.invoice.select
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `field`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 7

### `view_account_invoice_filter`
- Name: account.invoice.select
- Model: `account.move`
- Type: inferred from arch
- Root tag: `search`
- Field references: 13
- Sample fields: `activity_type_id`, `activity_user_id`, `amount_total`, `date`, `invoice_user_id`, `journal_group_id`, `journal_id`, `line_ids`, `name`, `next_payment_date`, and 3 more
- XPath or positional patches: 0

### `view_account_move_filter`
- Name: account.move.select
- Model: `account.move`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `amount_total`, `date`, `invoice_date`, `journal_id`, `name`, `partner_id`, `ref`
- XPath or positional patches: 0

### `account_move_view_activity`
- Name: account.move.view.activity
- Model: `account.move`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 5
- Sample fields: `amount_total`, `commercial_partner_id`, `currency_id`, `name`, `state`
- XPath or positional patches: 0

### `view_move_form`
- Name: account.move.form
- Model: `account.move`
- Type: inferred from arch
- Root tag: `form`
- Field references: 110
- Sample fields: `account_id`, `account_internal_group`, `account_type`, `adjusting_entries_count`, `adjusting_entry_origin_label`, `adjusting_entry_origin_moves_count`, `alerts`, `amount_currency`, `amount_residual`, `analytic_distribution`, and 100 more
- Buttons: `%(action_view_account_move_reversal)d`, `action_activate_currency`, `action_add_from_catalog`, `action_automatic_entry`, `action_invoice_sent`, `action_open_business_doc`, `action_post`, `action_print_pdf`, `action_register_payment`, `action_reverse`, and 13 more
- XPath or positional patches: 0

### `view_account_move_kanban`
- Name: account.move.kanban
- Model: `account.move`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `activity_ids`, `amount_total_in_currency_signed`, `checked`, `currency_id`, `date`, `journal_id`, `name`, `partner_id`, `state`
- XPath or positional patches: 0

### `view_in_invoice_refund_tree`
- Name: account.out.invoice.list
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_in_invoice_tree`
- Root tag: `field`
- Field references: 1
- Sample fields: `currency_id`
- XPath or positional patches: 0

### `view_in_invoice_bill_tree`
- Name: account.out.invoice.list
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_in_invoice_tree`
- Root tag: `field`
- Field references: 1
- Sample fields: `currency_id`
- XPath or positional patches: 0

### `view_in_invoice_tree`
- Name: account.out.invoice.list
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_out_credit_note_tree`
- Name: account.out.invoice.list
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `button`
- Field references: 1
- Sample fields: `currency_id`
- Buttons: `action_force_register_payment`, `action_send_and_print`
- XPath or positional patches: 0

### `view_out_invoice_tree`
- Name: account.out.invoice.list
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `button`
- Field references: 1
- Sample fields: `currency_id`
- Buttons: `action_force_register_payment`, `action_send_and_print`
- XPath or positional patches: 0

### `view_duplicated_moves_tree_js`
- Name: account.duplicated.moves.list.js
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `display_name`
- XPath or positional patches: 3

### `view_invoice_tree`
- Name: account.invoice.list
- Model: `account.move`
- Type: inferred from arch
- Root tag: `list`
- Field references: 25
- Sample fields: `abnormal_amount_warning`, `abnormal_date_warning`, `activity_ids`, `amount_residual_signed`, `amount_tax_signed`, `amount_total_in_currency_signed`, `amount_untaxed_in_currency_signed`, `checked`, `company_currency_id`, `company_id`, and 15 more
- Buttons: `action_force_register_payment`
- XPath or positional patches: 0

### `view_move_tree_multi_edit`
- Name: account.move.list.multi.edit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_move_tree`
- Name: account.move.list
- Model: `account.move`
- Type: inferred from arch
- Root tag: `list`
- Field references: 14
- Sample fields: `activity_ids`, `amount_total_signed`, `checked`, `company_currency_id`, `company_id`, `currency_id`, `date`, `invoice_date`, `journal_id`, `made_sequence_gap`, and 4 more
- XPath or positional patches: 0

### `view_account_move_line_payment_filter`
- Name: account.move.line.payment.search
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 8
- Sample fields: `company_currency_id`, `currency_id`, `journal_id`, `move_id`, `name`, `partner_id`, `payment_date`, `ref`
- XPath or positional patches: 0

### `view_move_line_payment_tree`
- Name: account.move.line.payment.list
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 21
- Sample fields: `amount_residual`, `amount_residual_currency`, `company_currency_id`, `company_id`, `currency_id`, `date`, `date_maturity`, `discount_amount_currency`, `discount_date`, `invoice_date`, and 11 more
- Buttons: `action_payment_items_register_payment`, `edit`
- XPath or positional patches: 0

### `view_account_move_line_filter`
- Name: account.move.line.search
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 19
- Sample fields: `account_id`, `account_root_id`, `account_type`, `balance`, `date`, `date_maturity`, `discount_date`, `invoice_date`, `journal_group_id`, `journal_id`, and 9 more
- XPath or positional patches: 0

### `account_move_line_graph_date`
- Name: account.move.line.graph
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `balance`, `date`
- XPath or positional patches: 0

### `view_move_line_tax_audit_tree`
- Name: account.move.line.tax.audit.list
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `field`
- Field references: 7
- Sample fields: `analytic_distribution`, `credit`, `debit`, `journal_id`, `matching_number`, `tax_base_amount`, `tax_line_id`
- XPath or positional patches: 0

### `view_move_line_tree_grouped_partner`
- Name: account.move.line.list.grouped.partner
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `balance`, `date_maturity`, `partner_id`
- XPath or positional patches: 0

### `view_move_line_tree_grouped_general`
- Name: account.move.line.list.grouped.misc
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `account_id`, `balance`
- XPath or positional patches: 0

### `view_move_line_tree_grouped_misc`
- Name: account.move.line.list.grouped.misc
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `field`
- Field references: 1
- Sample fields: `date`
- XPath or positional patches: 0

### `view_move_line_tree_grouped_bank_cash`
- Name: account.move.line.list.grouped.bank.cash
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `field`
- Field references: 1
- Sample fields: `date`
- XPath or positional patches: 0

### `view_move_line_tree_grouped_sales_purchases`
- Name: account.move.line.list.grouped.sales.purchase
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `date`, `tax_tag_ids`
- XPath or positional patches: 0

### `view_move_line_tree`
- Name: account.move.line.list
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 35
- Sample fields: `account_id`, `account_type`, `amount_currency`, `amount_residual`, `amount_residual_currency`, `analytic_distribution`, `balance`, `company_currency_id`, `company_id`, `credit`, and 25 more
- Buttons: `edit`
- XPath or positional patches: 0

### `view_move_line_pivot`
- Name: account.move.line.pivot
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `balance`, `date`, `journal_id`
- XPath or positional patches: 0

### `account_move_line_view_kanban_mobile`
- Name: account.move.line.kanban.mobile
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account_move_line_view_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `account_move_line_view_kanban`
- Name: account.move.line.kanban
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `account_id`, `company_currency_id`, `credit`, `date_maturity`, `debit`, `name`, `partner_id`, `tax_ids`
- XPath or positional patches: 0

### `view_move_line_form`
- Name: account.move.line.form
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 23
- Sample fields: `account_id`, `amount_currency`, `analytic_distribution`, `analytic_line_ids`, `balance`, `company_id`, `credit`, `currency_id`, `date`, `date_maturity`, and 13 more
- Buttons: `open_reconcile_view`
- XPath or positional patches: 0

## Actions

- `action_move_out_refund_type`: `act_window` Credit Notes
- `accountant_confirm_entries_action`: `server` Review Entries
- `action_check_hash_integrity`: `server` Data Inalterability Check
- `action_move_block_payment`: `server` (Un)Block Payment
- `action_move_force_register_payment`: `server` Pay
- `action_move_switch_move_type`: `server` Switch into invoice/credit note
- `action_move_line_form`: `act_window` Entries
- `action_amounts_to_settle`: `act_window` Amounts to Settle
- `action_move_in_refund_type`: `act_window` Refunds
- `action_move_in_invoice`: `act_window` Bills
- `action_move_in_invoice_type`: `act_window` Bills
- `action_move_out_refund_type_non_legacy`: `act_window` Credit Notes
- `action_move_out_invoice`: `act_window` Invoices
- `action_move_out_invoice_type`: `act_window` Invoices
- `action_account_moves_email_preview`: `act_window` Journal Entries
- `action_move_journal_line`: `act_window` Journal Entries
- `action_account_moves_all`: `act_window` Journal Items
- `action_account_moves_all_tree`: `act_window` Journal Items
- `action_account_moves_ledger_partner`: `act_window` Partner Ledger
- `action_account_moves_journal_misc`: `act_window` Miscellaneous

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
