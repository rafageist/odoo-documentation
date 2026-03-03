<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_product_view_form_normalized_account`
- Name: product.product.view.form.normalized.account.inherit
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_product_view_form_normalized`
- Root tag: `field`
- Field references: 3
- Sample fields: `list_price`, `tax_string`, `taxes_id`
- XPath or positional patches: 0

### `product_view_search_catalog`
- Name: product.view.search.catalog.inherit.account
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_view_search_catalog`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `seller_ids`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
