---
tags: [odoo, community, generated, views]
---

# views/product_attribute_views.xml

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `views/product_attribute_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `attribute_tree_view`
- Name: product.attribute.list
- Model: `product.attribute`
- Type: inferred from arch
- Inherits: `product.attribute_tree_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `create_variant`, `visibility`
- XPath or positional patches: 0

### `product_attribute_view_form`
- Name: product.attribute.view.form
- Model: `product.attribute`
- Type: inferred from arch
- Inherits: `product.product_attribute_view_form`
- Root tag: `group`
- Field references: 3
- Sample fields: `is_thumbnail_visible`, `preview_variants`, `visibility`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Views]]

