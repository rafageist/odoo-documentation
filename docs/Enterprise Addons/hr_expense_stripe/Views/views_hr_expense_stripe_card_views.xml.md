---
tags: [odoo, enterprise, generated, views]
---

# views/hr_expense_stripe_card_views.xml

- Module: [[docs/Enterprise Addons/hr_expense_stripe/hr_expense_stripe|hr_expense_stripe]]
- Scope: Enterprise Addons
- Source file: `views/hr_expense_stripe_card_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `hr_expense_stripe_card_view_search`
- Name: hr.expense.stripe.card.view.search
- Model: `hr.expense.stripe.card`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `employee_id`, `last_4`, `name`
- XPath or positional patches: 0

### `view_hr_expense_stripe_card_kanban`
- Name: hr.expense.stripe.card.view.kanban
- Model: `hr.expense.stripe.card`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `card_number_public`, `card_type`, `expiration`, `name`
- XPath or positional patches: 0

### `view_hr_expense_stripe_card_list`
- Name: hr.expense.stripe.card.view.list
- Model: `hr.expense.stripe.card`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `card_type`, `company_id`, `currency_id`, `employee_id`, `journal_id`, `last_4`, `name`, `spending_policy_category_tag_ids`, `spending_policy_country_tag_ids`, `spending_policy_interval`, and 3 more
- XPath or positional patches: 0

### `view_hr_expense_stripe_card_form`
- Name: hr.expense.stripe.card.view.form
- Model: `hr.expense.stripe.card`
- Type: inferred from arch
- Root tag: `form`
- Field references: 18
- Sample fields: `card_number_public`, `card_type`, `company_id`, `currency_id`, `delivery_address_id`, `employee_id`, `employee_name`, `expenses_count`, `expiration`, `journal_id`, and 8 more
- Buttons: `action_activate_card`, `action_block_card`, `action_open_cardholder_wizard`, `action_open_employee`, `action_open_expenses`, `action_pause_card`, `action_pause_card_warning_view`
- XPath or positional patches: 0

## Actions

- `action_hr_expense_stripe_card`: `act_window` Cards

## Menus

- `menu_hr_expense_stripe_card`: Cards

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_expense_stripe/Views]]

