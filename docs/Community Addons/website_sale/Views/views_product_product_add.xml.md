<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_product_add.xml

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `views/product_product_add.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_product_view_form_normalized`
- Name: product.product.view.form.normalized.website.sale
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_product_view_form_normalized`
- Root tag: `div`
- Field references: 1
- Sample fields: `public_categ_ids`
- XPath or positional patches: 1

### `product_product_view_form_normalized_website_sale`
- Name: product.product.view.form.normalized.website.sale.inherit
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_product_view_form_normalized`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `website_url`
- XPath or positional patches: 2

## Actions

- `product_product_action_add`: `act_window` New Product

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Views]]

<!-- GENERATED:VIEWFILE -->
