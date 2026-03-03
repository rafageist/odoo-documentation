---
tags: [odoo, community, generated, views]
---

# views/pos_preset_view.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/pos_preset_view.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_pos_preset_tree`
- Name: pos.preset.list
- Model: `pos.preset`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `color`, `identification`, `name`, `use_timing`
- XPath or positional patches: 0

### `view_pos_preset_form`
- Name: pos.preset.form
- Model: `pos.preset`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `attendance_ids`, `color`, `count_linked_config`, `count_linked_orders`, `fiscal_position_id`, `identification`, `image_512`, `interval_time`, `is_return`, `name`, and 4 more
- Buttons: `action_open_linked_config`, `action_open_linked_orders`
- XPath or positional patches: 0

## Actions

- `action_pos_preset_form`: `act_window` Presets

## Menus

- `menu_pos_preset`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

