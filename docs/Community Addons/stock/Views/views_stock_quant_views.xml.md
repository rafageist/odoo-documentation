<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_quant_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_quant_views.xml`
- Views: 9
- Actions: 6
- Menus: 2
- Rules: 0

## View records

### `view_stock_quant_tree_inventory_editable`
- Name: stock.quant.inventory.list.editable
- Model: `stock.quant`
- Type: inferred from arch
- Root tag: `list`
- Field references: 23
- Sample fields: `company_id`, `create_date`, `cyclic_inventory_frequency`, `id`, `inventory_date`, `inventory_diff_quantity`, `inventory_quantity`, `inventory_quantity_set`, `is_outdated`, `last_count_date`, and 13 more
- Buttons: `action_apply_all`, `action_apply_inventory`, `action_clear_inventory_quantity`, `action_inventory_history`, `action_reset`, `stock.action_stock_inventory_adjustement_name`, `stock.action_stock_request_count`
- XPath or positional patches: 0

### `view_stock_quant_form`
- Name: view.stock.quant.form
- Model: `stock.quant`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `company_id`, `location_id`, `lot_id`, `owner_id`, `package_id`, `product_id`
- XPath or positional patches: 0

### `stock_quant_view_graph`
- Name: stock.quant.graph
- Model: `stock.quant`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `location_id`, `quantity`
- XPath or positional patches: 0

### `view_stock_quant_pivot`
- Name: stock.quant.pivot
- Model: `stock.quant`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `location_id`, `product_id`, `quantity`
- XPath or positional patches: 0

### `view_stock_quant_tree`
- Name: stock.quant.list
- Model: `stock.quant`
- Type: inferred from arch
- Inherits: `stock.view_stock_quant_tree_simple`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_stock_quant_tree_simple`
- Name: stock.quant.list
- Model: `stock.quant`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `available_quantity`, `company_id`, `location_id`, `lot_id`, `lot_properties`, `owner_id`, `package_id`, `product_id`, `product_uom_id`, `quantity`
- XPath or positional patches: 0

### `view_stock_quant_tree_editable`
- Name: stock.quant.list.editable
- Model: `stock.quant`
- Type: inferred from arch
- Root tag: `list`
- Field references: 17
- Sample fields: `available_quantity`, `company_id`, `create_date`, `id`, `inventory_quantity_auto_apply`, `location_id`, `lot_id`, `lot_properties`, `owner_id`, `package_id`, and 7 more
- Buttons: `action_stock_quant_relocate`, `action_view_orderpoints`, `action_view_stock_moves`
- XPath or positional patches: 0

### `view_stock_quant_form_editable`
- Name: stock.quant.form.editable
- Model: `stock.quant`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `available_quantity`, `company_id`, `location_id`, `lot_id`, `owner_id`, `package_id`, `product_id`, `product_uom_id`, `quantity`, `reserved_quantity`, and 1 more
- XPath or positional patches: 0

### `quant_search_view`
- Name: stock.quant.search
- Model: `stock.quant`
- Type: inferred from arch
- Root tag: `search`
- Field references: 12
- Sample fields: `inventory_date`, `location_id`, `lot_id`, `lot_properties`, `owner_id`, `package_id`, `product_categ_id`, `product_id`, `product_tmpl_id`, `storage_category_id`, and 2 more
- XPath or positional patches: 0

## Actions

- `action_stock_quant_relocate`: `server` Relocate
- `action_view_set_to_zero_quants_tree`: `server` Set to 0
- `action_view_set_quants_tree`: `server` Set to quantity on hand
- `stock_quant_action`: `act_window` Locations
- `action_view_quants`: `server` Inventory
- `action_view_inventory_tree`: `server` Inventory

## Menus

- `menu_valuation`: Locations
- `menu_action_inventory_tree`: Physical Inventory

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

<!-- GENERATED:VIEWFILE -->
