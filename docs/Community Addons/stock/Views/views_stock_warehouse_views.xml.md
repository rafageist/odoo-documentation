---
tags: [odoo, community, generated, views]
---

# views/stock_warehouse_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_warehouse_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `stock_warehouse_view_search`
- Name: stock.warehouse.search
- Model: `stock.warehouse`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_warehouse_tree`
- Name: stock.warehouse.list
- Model: `stock.warehouse`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `active`, `company_id`, `lot_stock_id`, `name`, `partner_id`, `sequence`
- XPath or positional patches: 0

### `view_warehouse`
- Name: stock.warehouse
- Model: `stock.warehouse`
- Type: inferred from arch
- Root tag: `form`
- Field references: 22
- Sample fields: `active`, `code`, `company_id`, `delivery_steps`, `in_type_id`, `int_type_id`, `lot_stock_id`, `name`, `out_type_id`, `pack_type_id`, and 12 more
- Buttons: `action_view_all_routes`
- XPath or positional patches: 0

## Actions

- `action_warehouse_form`: `act_window` Warehouses

## Menus

- `menu_action_warehouse_form`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

