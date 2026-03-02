<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_expense_stripe_card_views.xml

- Module: [[docs/Enterprise Addons/hr_expense_stripe_demo/hr_expense_stripe_demo|hr_expense_stripe_demo]]
- Scope: Enterprise Addons
- Source file: `views/hr_expense_stripe_card_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_hr_expense_stripe_card_tree_inherit_demo`
- Name: hr.expense.stripe.card.view.list.inherit.demo
- Model: `hr.expense.stripe.card`
- Type: inferred from arch
- Inherits: `hr_expense_stripe.view_hr_expense_stripe_card_list`
- Root tag: `field`
- Field references: 1
- Sample fields: `last_4`
- XPath or positional patches: 0

### `view_hr_expense_stripe_card_form_inherit_demo`
- Name: hr.expense.stripe.card.view.form.inherit.demo
- Model: `hr.expense.stripe.card`
- Type: inferred from arch
- Inherits: `hr_expense_stripe.view_hr_expense_stripe_card_form`
- Root tag: `header`
- Field references: 0
- Buttons: `action_create_test_purchase`, `action_open_shipping_wizard`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_expense_stripe_demo/Views]]

<!-- GENERATED:VIEWFILE -->
