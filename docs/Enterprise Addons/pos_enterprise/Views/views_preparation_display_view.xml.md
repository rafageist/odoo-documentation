---
tags: [odoo, enterprise, generated, views]
---

# views/preparation_display_view.xml

- Module: [[docs/Enterprise Addons/pos_enterprise/pos_enterprise|pos_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/preparation_display_view.xml`
- Views: 4
- Actions: 4
- Menus: 2
- Rules: 0

## View records

### `preparation_display_view_kanban`
- Name: preparation.display.kanban.view
- Model: `pos.prep.display`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `average_time`, `name`, `order_count`, `stage_ids`
- Buttons: `open_ui`
- XPath or positional patches: 0

### `preparation_display_view_search`
- Name: preparation.display.search.view
- Model: `pos.prep.display`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `pos_config_ids`
- XPath or positional patches: 0

### `preparation_display_view_tree`
- Name: preparation.display.list.view
- Model: `pos.prep.display`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `category_ids`, `name`, `pos_config_ids`, `stage_ids`
- XPath or positional patches: 0

### `preparation_display_view_form`
- Name: preparation.display.form.view
- Model: `pos.prep.display`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `alert_timer`, `auto_clear`, `category_ids`, `clear_time_interval`, `color`, `name`, `pos_config_ids`, `sequence`, `stage_ids`
- XPath or positional patches: 0

## Actions

- `action_pos_preparation_display_bar_restaurant_filter_link`: `act_url` Preparation Display
- `action_preparation_display_bar_restaurant_filter`: `act_window` Preparation Display
- `action_pos_preparation_display_kitchen_display`: `server` Kitchen Display
- `action_preparation_display`: `act_window` Preparation Display

## Menus

- `menu_point_kitchen_display_root`: Kitchen Display
- `point_of_sale.menu_pos_preparation_display`: Preparation Display

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_enterprise/Views]]

