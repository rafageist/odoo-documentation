---
tags: [odoo, community, generated, views]
---

# wizard/stock_replenishment_info.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `wizard/stock_replenishment_info.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `replenishment_option_warning_view`
- Name: stock.replenishment.warning.view
- Model: `stock.replenishment.option`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `free_qty`, `qty_to_order`, `warning_message`
- Buttons: `order_all`, `order_avbl`
- XPath or positional patches: 0

### `replenishment_option_tree_view`
- Name: stock.replenishment.option.list.view
- Model: `stock.replenishment.option`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `free_qty`, `lead_time`, `location_id`, `qty_to_order`, `route_id`, `uom`, `warehouse_id`
- Buttons: `select_route`
- XPath or positional patches: 0

### `view_stock_replenishment_info`
- Name: Stock Replenishment Information
- Model: `stock.replenishment.info`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `based_on`, `json_lead_days`, `json_replenishment_graph`, `orderpoint_id`, `percent_factor`, `product_max_qty`, `product_min_qty`, `product_uom_name`, `qty_to_order`, `warehouseinfo_ids`, and 1 more
- XPath or positional patches: 0

## Actions

- `action_stock_replenishment_info`: `act_window` Replenishment Information

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

