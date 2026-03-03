---
tags: [odoo, community, generated, views]
---

# views/pos_restaurant_views.xml

- Module: [[docs/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]]
- Scope: Community Addons
- Source file: `views/pos_restaurant_views.xml`
- Views: 5
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_restaurant_table_form`
- Name: Restaurant Table
- Model: `restaurant.table`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `color`, `height`, `position_h`, `position_v`, `seats`, `shape`, `table_number`, `width`
- XPath or positional patches: 0

### `view_restaurant_floor_kanban`
- Name: restaurant.floor.kanban
- Model: `restaurant.floor`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `name`, `pos_config_ids`
- XPath or positional patches: 0

### `view_restaurant_floor_search`
- Name: restaurant.floor.search
- Model: `restaurant.floor`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_restaurant_floor_tree`
- Name: Restaurant Floors
- Model: `restaurant.floor`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `name`, `pos_config_ids`, `sequence`
- XPath or positional patches: 0

### `view_restaurant_floor_form`
- Name: Restaurant Floors
- Model: `restaurant.floor`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `active`, `background_color`, `color`, `floor_background_image`, `height`, `name`, `pos_config_ids`, `seats`, `shape`, `table_ids`, and 2 more
- XPath or positional patches: 0

## Actions

- `action_restaurant_floor_form`: `act_window` Floor Plans

## Menus

- `menu_restaurant_floor_all`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/pos_restaurant/Views]]

