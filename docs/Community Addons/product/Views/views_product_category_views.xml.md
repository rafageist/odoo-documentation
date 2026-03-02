<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_category_views.xml

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Source file: `views/product_category_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_category_search_view`
- Name: product.category.search
- Model: `product.category`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `parent_id`
- XPath or positional patches: 0

### `product_category_list_view`
- Name: product.category.list
- Model: `product.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `display_name`
- XPath or positional patches: 0

### `product_category_form_view`
- Name: product.category.form
- Model: `product.category`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `name`, `parent_id`, `product_count`
- Buttons: `%(product_template_action_all)d`
- XPath or positional patches: 0

## Actions

- `product_category_action_form`: `act_window` Categories

## Navigation

- **Parent:** [[docs/Community Addons/product/Views]]

<!-- GENERATED:VIEWFILE -->
