---
tags: [odoo, enterprise, generated, views]
---

# views/product_views.xml

- Module: [[docs/Enterprise Addons/account_avatax/account_avatax|account_avatax]]
- Scope: Enterprise Addons
- Source file: `views/product_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_category_form_inherit`
- Name: product.category.form.inherit
- Model: `product.category`
- Type: inferred from arch
- Inherits: `product.product_category_form_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `avatax_category_id`, `parent_id`
- XPath or positional patches: 0

### `product_template_form_inherit`
- Name: product.template.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `div`
- Field references: 2
- Sample fields: `avatax_category_id`, `fiscal_country_codes`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_avatax/Views]]

