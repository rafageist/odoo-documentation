---
tags: [odoo, community, generated, views]
---

# views/pos_session_view.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/pos_session_view.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_pos_session_search`
- Name: pos.session.search.view
- Model: `pos.session`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `config_id`, `name`, `user_id`
- XPath or positional patches: 0

### `view_pos_session_kanban`
- Name: pos.session.kanban
- Model: `pos.session`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `config_id`, `name`, `start_at`, `state`, `user_id`
- XPath or positional patches: 0

### `view_pos_session_tree`
- Name: pos.session.list.view
- Model: `pos.session`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `cash_register_balance_end`, `cash_register_balance_end_real`, `cash_register_balance_start`, `config_id`, `name`, `start_at`, `state`, `stop_at`, `user_id`
- XPath or positional patches: 0

### `view_pos_session_form`
- Name: pos.session.form.view
- Model: `pos.session`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `cash_control`, `cash_register_balance_end_real`, `cash_register_balance_start`, `config_id`, `currency_id`, `failed_pickings`, `move_id`, `name`, `order_count`, `picking_count`, and 6 more
- Buttons: `action_pos_session_closing_control`, `action_show_payments_list`, `action_stock_picking`, `action_view_order`, `open_frontend_cb`, `show_cash_register`, `show_journal_items`
- XPath or positional patches: 0

## Actions

- `action_pos_session`: `act_window` Sessions

## Menus

- `menu_pos_session_all`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

