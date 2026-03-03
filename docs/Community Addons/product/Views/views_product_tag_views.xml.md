---
tags: [odoo, community, generated, views]
---

# views/product_tag_views.xml

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Source file: `views/product_tag_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_tag_tree_view`
- Name: product.tag.list
- Model: `product.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `color`, `image`, `name`, `product_product_ids`, `product_template_ids`, `sequence`, `visible_to_customers`
- XPath or positional patches: 0

### `product_tag_form_view`
- Name: product.tag.form
- Model: `product.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `color`, `image`, `name`, `visible_to_customers`
- XPath or positional patches: 0

## Actions

- `product_tag_action`: `act_window` Product Tags

## Navigation

- **Parent:** [[docs/Community Addons/product/Views]]

