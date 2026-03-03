---
tags: [odoo, enterprise, generated, views]
---

# views/product_views.xml

- Module: [[docs/Enterprise Addons/sale_amazon/sale_amazon|sale_amazon]]
- Scope: Enterprise Addons
- Source file: `views/product_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `amazon_product_product_view_form`
- Name: product.product.form.inherit
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_normal_form_view`
- Root tag: `div`
- Field references: 1
- Sample fields: `offer_count`
- Buttons: `action_view_offers`
- XPath or positional patches: 1

### `amazon_product_template_view_form`
- Name: product.template.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_only_form_view`
- Root tag: `div`
- Field references: 1
- Sample fields: `offer_count`
- Buttons: `action_view_offers`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_amazon/Views]]

