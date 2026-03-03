---
tags: [odoo, enterprise, generated, views]
---

# views/product_product_views.xml

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `views/product_product_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_normal_form_view`
- Name: sale.subscription.product.product.normal.form.inherit
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_normal_form_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `sale_subscription_product_view_search_catalog`
- Name: product.view.search.catalog.inherit.sale.subscription
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_view_search_catalog`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Views]]

