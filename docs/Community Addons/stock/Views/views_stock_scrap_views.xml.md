---
tags: [odoo, community, generated, views]
---

# views/stock_scrap_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_scrap_views.xml`
- Views: 5
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `stock_scrap_form_view2`
- Name: stock.scrap.form2
- Model: `stock.scrap`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `company_id`, `location_id`, `lot_id`, `owner_id`, `package_id`, `picking_id`, `product_id`, `product_uom_id`, `scrap_location_id`, `scrap_qty`, and 4 more
- Buttons: `action_validate`
- XPath or positional patches: 0

### `stock_scrap_tree_view`
- Name: stock.scrap.list
- Model: `stock.scrap`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `company_id`, `date_done`, `location_id`, `name`, `product_id`, `product_uom_id`, `scrap_location_id`, `scrap_qty`, `state`
- XPath or positional patches: 0

### `stock_scrap_view_kanban`
- Name: stock.scrap.kanban
- Model: `stock.scrap`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `date_done`, `name`, `product_id`, `scrap_qty`, `state`
- XPath or positional patches: 0

### `stock_scrap_form_view`
- Name: stock.scrap.form
- Model: `stock.scrap`
- Type: inferred from arch
- Root tag: `form`
- Field references: 18
- Sample fields: `company_id`, `date_done`, `location_id`, `lot_id`, `move_ids`, `name`, `origin`, `owner_id`, `package_id`, `picking_id`, and 8 more
- Buttons: `action_get_stock_move_lines`, `action_get_stock_picking`, `action_validate`
- XPath or positional patches: 0

### `stock_scrap_search_view`
- Name: stock.scrap.search
- Model: `stock.scrap`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `create_date`, `location_id`, `name`, `product_id`, `scrap_location_id`
- XPath or positional patches: 0

## Actions

- `action_stock_scrap`: `act_window` Scrap Orders

## Menus

- `menu_stock_scrap`: Scrap

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

