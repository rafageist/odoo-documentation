---
tags: [odoo, community, generated, views]
---

# views/pos_category_view.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/pos_category_view.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_pos_category_kanban`
- Name: pos.category.kanban
- Model: `pos.category`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `image_128`, `name`
- XPath or positional patches: 0

### `product_pos_category_tree_view`
- Name: pos.category.list
- Model: `pos.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `color`, `display_name`, `parent_id`, `sequence`
- XPath or positional patches: 0

### `product_pos_category_form_view`
- Name: pos.category.form
- Model: `pos.category`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `color`, `hour_after`, `hour_until`, `image_512`, `name`, `parent_id`
- XPath or positional patches: 0

## Actions

- `product_pos_category_action`: `act_window` PoS Product Categories

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

