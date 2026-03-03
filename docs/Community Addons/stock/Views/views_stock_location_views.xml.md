---
tags: [odoo, community, generated, views]
---

# views/stock_location_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_location_views.xml`
- Views: 8
- Actions: 5
- Menus: 2
- Rules: 0

## View records

### `stock_location_route_view_search`
- Name: stock.location.route.search
- Model: `stock.route`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `stock_location_route_form_view`
- Name: stock.location.route.form
- Model: `stock.route`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `action`, `active`, `company_id`, `location_dest_id`, `location_src_id`, `name`, `package_type_selectable`, `product_categ_selectable`, `product_selectable`, `rule_ids`, and 5 more
- XPath or positional patches: 0

### `stock_location_route_tree`
- Name: stock.location.route.list
- Model: `stock.route`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `active`, `company_id`, `name`, `sequence`
- XPath or positional patches: 0

### `stock_location_view_tree2_editable`
- Name: stock.location.list2.editable
- Model: `stock.location`
- Type: inferred from arch
- Inherits: `stock.view_location_tree2`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_location_tree2`
- Name: stock.location.list
- Model: `stock.location`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `active`, `company_id`, `complete_name`, `is_empty`, `storage_category_id`, `usage`
- XPath or positional patches: 0

### `view_location_search`
- Name: stock.location.search
- Model: `stock.location`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `complete_name`, `location_id`, `usage`, `warehouse_id`
- XPath or positional patches: 0

### `stock_location_view_form_editable`
- Name: stock.location.form.editable
- Model: `stock.location`
- Type: inferred from arch
- Inherits: `stock.view_location_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_location_form`
- Name: stock.location.form
- Model: `stock.location`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `active`, `company_id`, `cyclic_inventory_frequency`, `last_inventory_date`, `location_id`, `name`, `next_inventory_date`, `removal_strategy_id`, `replenish_location`, `storage_category_id`, and 1 more
- Buttons: `%(location_open_putaway)d`, `stock.act_product_location_open`
- XPath or positional patches: 0

## Actions

- `action_routes_form`: `act_window` Routes
- `action_prod_inv_location_form`: `act_window` Locations
- `action_location_form`: `act_window` Locations
- `action_storage_category_locations`: `act_window` Locations
- `act_product_location_open`: `act_window` Products

## Menus

- `menu_routes_config`: Routes
- `menu_action_location_form`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

