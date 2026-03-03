<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_payment_term_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/account_payment_term_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_account_payment_term_kanban`
- Name: account.payment.term.kanban
- Model: `account.payment.term`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `name`, `note`
- XPath or positional patches: 0

### `view_payment_term_form`
- Name: account.payment.term.form
- Model: `account.payment.term`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `active`, `company_id`, `days_next_month`, `delay_type`, `discount_days`, `discount_percentage`, `display_days_next_month`, `display_on_invoice`, `early_discount`, `early_pay_discount_computation`, and 11 more
- XPath or positional patches: 0

### `view_payment_term_tree`
- Name: account.payment.term.list
- Model: `account.payment.term`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `company_id`, `name`, `sequence`
- XPath or positional patches: 0

### `view_payment_term_search`
- Name: account.payment.term.search
- Model: `account.payment.term`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `active`, `name`
- XPath or positional patches: 0

## Actions

- `action_payment_term_form`: `act_window` Payment Terms

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
