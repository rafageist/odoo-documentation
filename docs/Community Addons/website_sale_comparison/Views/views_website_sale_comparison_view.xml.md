<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/website_sale_comparison_view.xml

- Module: [[docs/Community Addons/website_sale_comparison/website_sale_comparison|website_sale_comparison]]
- Scope: Community Addons
- Source file: `views/website_sale_comparison_view.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `product_attribute_view_form`
- Name: product.attribute.form.inherit
- Model: `product.attribute`
- Type: inferred from arch
- Inherits: `website_sale.product_attribute_view_form`
- Root tag: `group`
- Field references: 1
- Sample fields: `category_id`
- XPath or positional patches: 1

### `product_attribute_tree_view_inherit`
- Name: product.attribute.list.inherit
- Model: `product.attribute`
- Type: inferred from arch
- Inherits: `product.attribute_tree_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `category_id`, `name`
- XPath or positional patches: 0

### `product_attribute_category_tree_view`
- Name: product.attribute.category.list
- Model: `product.attribute.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `attribute_ids`, `name`, `sequence`
- XPath or positional patches: 0

## Actions

- `product_attribute_category_action`: `act_window` Attribute Categories

## Menus

- `menu_attribute_category_action`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/website_sale_comparison/Views]]

<!-- GENERATED:VIEWFILE -->
