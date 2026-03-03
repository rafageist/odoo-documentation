---
tags: [odoo, community, generated, views]
---

# views/point_of_sale_dashboard.xml

- Module: [[docs/Community Addons/pos_self_order/pos_self_order|pos_self_order]]
- Scope: Community Addons
- Source file: `views/point_of_sale_dashboard.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `pos_self_order_menu_item`
- Name: pos.config.kanban.view.inherit.self_order
- Model: `pos.config`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_config_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `current_session_id`, `self_ordering_mode`
- Buttons: `action_close_kiosk_session`, `action_open_wizard`, `preview_self_order_app`
- XPath or positional patches: 3

### `pos_self_order_search_view`
- Name: pos.self.order.search.view
- Model: `pos.config`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_config_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `action_pos_self_order_search_view`: `act_window` Kiosk

## Navigation

- **Parent:** [[docs/Community Addons/pos_self_order/Views]]

