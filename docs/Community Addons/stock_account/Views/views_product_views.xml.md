---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/stock_account/stock_account|stock_account]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_product_stock_tree_inherit_stock_account`
- Name: product.product.stock.list.inherit.stock.account
- Model: `product.product`
- Type: inferred from arch
- Inherits: `stock.product_product_stock_tree`
- Root tag: `field`
- Field references: 5
- Sample fields: `avg_cost`, `company_currency_id`, `cost_method`, `qty_available`, `total_value`
- XPath or positional patches: 0

### `view_template_property_form_stock_account`
- Name: view.template.property.form.stock.account
- Model: `product.template`
- Type: inferred from arch
- Inherits: `stock.view_template_property_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `lot_valuated`
- XPath or positional patches: 1

### `view_category_property_form`
- Name: product.category.stock.property.form.inherit
- Model: `product.category`
- Type: inferred from arch
- Inherits: `account.view_category_property_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `property_account_expense_categ_id`, `property_price_difference_account_id`, `property_stock_valuation_account_id`
- XPath or positional patches: 0

### `view_category_property_form_stock`
- Name: product.category.stock.property.form.inherit.stock
- Model: `product.category`
- Type: inferred from arch
- Inherits: `stock.product_category_form_view_inherit`
- Root tag: `group`
- Field references: 2
- Sample fields: `property_cost_method`, `property_valuation`
- XPath or positional patches: 1

### `product_template_tree_view`
- Name: product.template.list.inherit.stock.account
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_tree_view`
- Root tag: `field`
- Field references: 1
- Sample fields: `standard_price`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/stock_account/Views]]

