---
tags: [odoo, enterprise, generated, views]
---

# views/product_mcc_stripe_tag_views.xml

- Module: [[docs/Enterprise Addons/hr_expense_stripe/hr_expense_stripe|hr_expense_stripe]]
- Scope: Enterprise Addons
- Source file: `views/product_mcc_stripe_tag_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_product_mcc_stripe_tag_search`
- Name: product.mcc.stripe.tag.view.search
- Model: `product.mcc.stripe.tag`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `code`, `name`, `product_name`
- XPath or positional patches: 0

### `view_product_mcc_stripe_tag_list`
- Name: product.mcc.stripe.tag.view.list
- Model: `product.mcc.stripe.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `code`, `name`, `product_id`
- XPath or positional patches: 0

### `view_product_mcc_stripe_tag_form`
- Name: product.mcc.stripe.tag.view.form
- Model: `product.mcc.stripe.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `code`, `name`, `product_id`, `stripe_name`
- XPath or positional patches: 0

## Actions

- `product_mcc_stripe_tag`: `act_window` Stripe Merchant Category Codes

## Menus

- `menu_product_mcc_stripe_tag`: MCC

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_expense_stripe/Views]]

