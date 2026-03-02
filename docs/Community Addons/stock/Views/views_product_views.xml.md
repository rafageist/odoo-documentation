<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 14
- Actions: 7
- Menus: 3
- Rules: 0

## View records

### `product_search_form_view_stock_report`
- Name: product.product.search.stock.form.stock.report
- Model: `product.product`
- Type: inferred from arch
- Inherits: `stock_product_search_form_view`
- Root tag: `filter`
- Field references: 1
- Sample fields: `categ_id`
- XPath or positional patches: 3

### `product_product_stock_tree`
- Name: product.product.stock.list
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `categ_id`, `display_name`, `free_qty`, `id`, `incoming_qty`, `outgoing_qty`, `qty_available`, `uom_id`, `virtual_available`
- Buttons: `%(action_inventory_at_date)d`, `%(action_view_quants)d`, `%(stock_move_line_action)d`, `action_product_forecast_report`, `action_view_orderpoints`
- XPath or positional patches: 0

### `product_template_form_view_procurement_button`
- Name: product.template_procurement
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_only_form_view`
- Root tag: `data`
- Field references: 12
- Sample fields: `nbr_moves_in`, `nbr_moves_out`, `nbr_reordering_rules`, `qty_available`, `reordering_max_qty`, `reordering_min_qty`, `responsible_id`, `show_forecasted_qty_status_button`, `show_on_hand_qty_status_button`, `tracking`, and 2 more
- Buttons: `action_open_documents`, `action_open_product_lot`, `action_product_tmpl_forecast_report`, `action_view_orderpoints`, `action_view_related_putaway_rules`, `action_view_stock_move_lines`, `action_view_storage_category_capacity`
- XPath or positional patches: 1

### `product_form_view_procurement_button`
- Name: product.product.procurement
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_normal_form_view`
- Root tag: `data`
- Field references: 11
- Sample fields: `nbr_moves_in`, `nbr_moves_out`, `nbr_reordering_rules`, `qty_available`, `reordering_max_qty`, `reordering_min_qty`, `show_forecasted_qty_status_button`, `show_on_hand_qty_status_button`, `tracking`, `uom_name`, and 1 more
- Buttons: `action_open_product_lot`, `action_product_forecast_report`, `action_view_orderpoints`, `action_view_related_putaway_rules`, `action_view_stock_move_lines`, `action_view_storage_category_capacity`
- XPath or positional patches: 2

### `product_view_kanban_catalog`
- Name: product.view.kanban.catalog.inherit.stock
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_view_kanban_catalog`
- Root tag: `field`
- Field references: 5
- Sample fields: `free_qty`, `id`, `is_storable`, `product_template_attribute_value_ids`, `qty_available`
- XPath or positional patches: 1

### `product_search_form_view_stock`
- Name: product.search.stock.form
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_search_form_view`
- Root tag: `filter`
- Field references: 2
- Sample fields: `location_id`, `warehouse_id`
- XPath or positional patches: 1

### `product_template_kanban_stock_view`
- Name: Product Template Kanban Stock
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_kanban_view`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `qty_available`, `show_on_hand_qty_status_button`, `uom_id`
- XPath or positional patches: 2

### `view_template_property_form`
- Name: product.template.stock.property.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `field`
- Field references: 17
- Sample fields: `description_picking`, `description_pickingin`, `description_pickingout`, `has_available_route_ids`, `is_storable`, `next_serial`, `product_tooltip`, `property_stock_inventory`, `property_stock_production`, `qty_available`, and 7 more
- Buttons: `%(action_open_routes)d`
- XPath or positional patches: 5

### `stock_product_search_form_view`
- Name: product.product.search.stock.form
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_search_form_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `product_template_search_view_inherit_stock`
- Name: product.template.search.inherit.stock
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `product_template_search_form_view_stock`
- Name: product.template.search.stock.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `field`
- Field references: 3
- Sample fields: `attribute_line_ids`, `location_id`, `warehouse_id`
- XPath or positional patches: 0

### `view_stock_product_template_tree`
- Name: product.template.stock.list.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_tree_view`
- Root tag: `field`
- Field references: 6
- Sample fields: `default_code`, `qty_available`, `responsible_id`, `show_on_hand_qty_status_button`, `uom_id`, `virtual_available`
- XPath or positional patches: 0

### `view_stock_product_tree`
- Name: product.stock.list.inherit
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_product_tree_view`
- Root tag: `field`
- Field references: 3
- Sample fields: `qty_available`, `type`, `virtual_available`
- XPath or positional patches: 0

### `product_category_form_view_inherit`
- Name: product.category.form
- Model: `product.category`
- Type: inferred from arch
- Inherits: `product.product_category_form_view`
- Root tag: `div`
- Field references: 4
- Sample fields: `packaging_reserve_method`, `parent_route_ids`, `removal_strategy_id`, `route_ids`
- Buttons: `%(category_open_putaway)d`
- XPath or positional patches: 2

## Actions

- `stock_product_normal_action`: `act_window` Product Variants
- `product_template_action_product`: `act_window` Products
- `action_product_stock_view`: `act_window` Stock
- `action_inventory_at_date`: `act_window` Inventory at Date
- `action_product_template_replenishment`: `server` Replenish
- `action_product_replenishment`: `server` Replenish
- `action_open_routes`: `server` Routes

## Menus

- `menu_product_stock`: Stock
- `product_product_menu`: Product Variants
- `menu_product_variant_config_stock`: Products

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

<!-- GENERATED:VIEWFILE -->
