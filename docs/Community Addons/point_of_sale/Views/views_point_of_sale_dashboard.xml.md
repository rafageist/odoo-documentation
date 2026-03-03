---
tags: [odoo, community, generated, views]
---

# views/point_of_sale_dashboard.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/point_of_sale_dashboard.xml`
- Views: 1
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `view_pos_config_kanban`
- Name: pos.config.kanban.view
- Model: `pos.config`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 14
- Sample fields: `access_token`, `cash_control`, `currency_id`, `current_session_id`, `current_session_state`, `current_user_id`, `last_session_closing_cash`, `last_session_closing_date`, `name`, `number_of_rescue_session`, and 4 more
- Buttons: `open_existing_session_cb`, `open_ui`
- XPath or positional patches: 0

## Actions

- `action_report_pos_order_all_filtered`: `act_window` Orders Analysis
- `action_pos_order_filtered`: `act_window` Orders
- `action_pos_session_filtered`: `act_window` Sessions

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

