<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_orderpoint_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_orderpoint_views.xml`
- Views: 6
- Actions: 3
- Menus: 1
- Rules: 0

## View records

### `view_warehouse_orderpoint_tree_editable_show_trigger`
- Name: stock.warehouse.orderpoint.list.editable.inherit.show_trigger
- Model: `stock.warehouse.orderpoint`
- Type: inferred from arch
- Inherits: `stock.view_warehouse_orderpoint_tree_editable`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_warehouse_orderpoint_form`
- Name: stock.warehouse.orderpoint.form
- Model: `stock.warehouse.orderpoint`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `active`, `allowed_location_ids`, `company_id`, `location_id`, `name`, `product_id`, `product_max_qty`, `product_min_qty`, `product_uom_name`, `replenishment_uom_id`, and 2 more
- Buttons: `stock.action_stock_replenishment_info`
- XPath or positional patches: 0

### `warehouse_orderpoint_search`
- Name: stock.warehouse.orderpoint.search
- Model: `stock.warehouse.orderpoint`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `location_id`, `name`, `product_id`, `trigger`, `warehouse_id`
- XPath or positional patches: 0

### `stock_reorder_report_search`
- Name: stock.warehouse.orderpoint.reorder.search
- Model: `stock.warehouse.orderpoint`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `effective_route_id`, `location_id`, `product_category_id`, `product_id`, `trigger`, `warehouse_id`
- XPath or positional patches: 0

### `view_warehouse_orderpoint_tree_editable`
- Name: stock.warehouse.orderpoint.list.editable
- Model: `stock.warehouse.orderpoint`
- Type: inferred from arch
- Root tag: `list`
- Field references: 21
- Sample fields: `active`, `company_id`, `deadline_date`, `location_id`, `product_category_id`, `product_id`, `product_max_qty`, `product_min_qty`, `product_tmpl_id`, `product_uom_name`, and 11 more
- Buttons: `%(action_orderpoint_snooze)d`, `action_product_forecast_report`, `action_remove_manual_qty_to_order`, `action_replenish`, `action_replenish_auto`, `action_stock_replenishment_info`
- XPath or positional patches: 0

### `view_stock_warehouse_orderpoint_kanban`
- Name: stock.warehouse.orderpoint.kanban
- Model: `stock.warehouse.orderpoint`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `name`, `product_id`, `product_max_qty`, `product_min_qty`
- XPath or positional patches: 0

## Actions

- `action_replenishment`: `server` Replenishment
- `action_orderpoint`: `act_window` Reordering Rules
- `action_orderpoint_replenish`: `act_window` Replenishment

## Menus

- `menu_reordering_rules_replenish`: Replenishment

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

<!-- GENERATED:VIEWFILE -->
