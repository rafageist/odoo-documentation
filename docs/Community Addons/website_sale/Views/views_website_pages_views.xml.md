---
tags: [odoo, community, generated, views]
---

# views/website_pages_views.xml

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `views/website_pages_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_pages_kanban_view`
- Name: Product Pages Kanban
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product_template_view_kanban_website_sale`
- Root tag: `kanban`
- Field references: 3
- Sample fields: `is_published`, `website_id`, `website_url`
- XPath or positional patches: 3

### `product_pages_tree_view`
- Name: Product Pages List
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product_template_view_tree_website_sale`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `default_code`, `is_published`, `is_seo_optimized`, `name`, `product_tag_ids`, `standard_price`, `website_id`, `website_url`
- XPath or positional patches: 2

## Actions

- `action_product_pages_list`: `act_window` Product Pages

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Views]]

