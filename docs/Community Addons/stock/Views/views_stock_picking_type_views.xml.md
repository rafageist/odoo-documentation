---
tags: [odoo, community, generated, views]
---

# views/stock_picking_type_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_picking_type_views.xml`
- Views: 4
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `stock_picking_type_kanban`
- Name: stock.picking.type.kanban
- Model: `stock.picking.type`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 12
- Sample fields: `code`, `color`, `count_move_ready`, `count_picking_backorders`, `count_picking_late`, `count_picking_ready`, `count_picking_waiting`, `is_favorite`, `kanban_dashboard_graph`, `name`, and 2 more
- Buttons: `get_action_picking_tree_ready`
- XPath or positional patches: 0

### `view_picking_type_form`
- Name: Operation Types
- Model: `stock.picking.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 32
- Sample fields: `active`, `auto_print_delivery_slip`, `auto_print_lot_labels`, `auto_print_package_label`, `auto_print_packages`, `auto_print_product_labels`, `auto_print_reception_report`, `auto_print_reception_report_labels`, `auto_print_return_slip`, `auto_show_reception_report`, and 22 more
- XPath or positional patches: 0

### `view_picking_type_tree`
- Name: Operation types
- Model: `stock.picking.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `active`, `company_id`, `name`, `sequence`, `sequence_id`, `warehouse_id`
- XPath or positional patches: 0

### `view_pickingtype_filter`
- Name: stock.picking.type.filter
- Model: `stock.picking.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `warehouse_id`
- XPath or positional patches: 0

## Actions

- `stock_picking_type_action`: `act_window` Inventory Overview
- `action_picking_type_list`: `act_window` Operations Types

## Menus

- `stock_picking_type_menu`: Overview
- `menu_pickingtype`: Operations Types

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

