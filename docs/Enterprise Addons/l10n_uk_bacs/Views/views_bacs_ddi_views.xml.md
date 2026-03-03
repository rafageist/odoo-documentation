---
tags: [odoo, enterprise, generated, views]
---

# views/bacs_ddi_views.xml

- Module: [[docs/Enterprise Addons/l10n_uk_bacs/l10n_uk_bacs|l10n_uk_bacs]]
- Scope: Enterprise Addons
- Source file: `views/bacs_ddi_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `account_bacs_ddi_search_view`
- Name: bacs.ddi.search
- Model: `bacs.ddi`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `name`, `partner_bank_id`, `partner_id`
- XPath or positional patches: 0

### `account_bacs_direct_debit_instruction_tree`
- Name: bacs.ddi.list
- Model: `bacs.ddi`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `name`, `partner_id`, `start_date`, `state`
- XPath or positional patches: 0

### `view_partner_bank_form_inherit_account_bacs`
- Name: res.partner.bank.view.form.inherit.account.bacs.direct.debit
- Model: `res.partner.bank`
- Type: inferred from arch
- Inherits: `base.view_partner_bank_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `partner_id`
- XPath or positional patches: 0

### `account_bacs_direct_debit_instruction_form`
- Name: bacs.ddi.form
- Model: `bacs.ddi`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `company_id`, `name`, `paid_invoices_len`, `partner_bank_id`, `partner_id`, `payment_journal_id`, `payments_len`, `start_date`, `state`, `suitable_journal_ids`
- Buttons: `action_cancel_draft_ddi`, `action_close_ddi`, `action_print_ddi`, `action_revoke_ddi`, `action_validate_ddi`, `action_view_paid_invoices`, `action_view_payments_to_collect`
- XPath or positional patches: 0

## Actions

- `account_bacs_direct_debit_instruction_tree_act`: `act_window` BACS Direct Debit Instruction

## Menus

- `account_bacs_direct_debit_customer_mandates_menu`: BACS Direct Debit Instructions

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_uk_bacs/Views]]

