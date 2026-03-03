<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_view.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/product_view.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_category_property_form`
- Name: product.category.property.form.inherit
- Model: `product.category`
- Type: inferred from arch
- Inherits: `product.product_category_form_view`
- Root tag: `group`
- Field references: 2
- Sample fields: `property_account_expense_categ_id`, `property_account_income_categ_id`
- XPath or positional patches: 1

### `product_template_form_view`
- Name: product.template.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `div`
- Field references: 7
- Sample fields: `fiscal_country_codes`, `property_account_expense_id`, `property_account_income_id`, `purchase_ok`, `supplier_taxes_id`, `tax_string`, `taxes_id`
- XPath or positional patches: 5

### `product_template_list_view_purchasable_inherit`
- Name: product.template.list.purchasable.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_list_view_purchasable`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `supplier_taxes_id`
- XPath or positional patches: 1

### `product_template_list_view_sellable_inherit`
- Name: product.template.list.sellable.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_list_view_sellable`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `taxes_id`
- XPath or positional patches: 1

## Actions

- `product_product_action_purchasable`: `act_window` Products
- `product_product_action_sellable`: `act_window` Products

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
