<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/product_product_views.xml

- Module: [[docs/Enterprise Addons/hr_expense_stripe/hr_expense_stripe|hr_expense_stripe]]
- Scope: Enterprise Addons
- Source file: `views/product_product_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_product_expense_view_form_inherits_stripe`
- Name: product.product.expense.inherit.stripe.form
- Model: `product.product`
- Type: inferred from arch
- Inherits: `hr_expense.product_product_expense_form_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `stripe_mcc_ids`
- XPath or positional patches: 1

### `product_product_view_form_inherits_stripe`
- Name: product.product.inherit.stripe.form
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_normal_form_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `stripe_mcc_ids`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_expense_stripe/Views]]

<!-- GENERATED:VIEWFILE -->
