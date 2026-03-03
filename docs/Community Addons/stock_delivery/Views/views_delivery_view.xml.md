---
tags: [odoo, community, generated, views]
---

# views/delivery_view.xml

- Module: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]
- Scope: Community Addons
- Source file: `views/delivery_view.xml`
- Views: 7
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `vpicktree_view_tree`
- Name: stock.picking.delivery.list.inherit.delivery
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `carrier_id`, `carrier_tracking_ref`, `destination_country_code`, `shipping_weight`, `weight`
- XPath or positional patches: 1

### `delivery_tracking_url_warning_form`
- Name: delivery.carrier.warning.url.form
- Model: `stock.picking`
- Type: inferred from arch
- Root tag: `form`
- Field references: 0
- XPath or positional patches: 0

### `stock_package_view_form`
- Name: stock.package.weight.form
- Model: `stock.package`
- Type: inferred from arch
- Inherits: `stock.stock_package_view_form`
- Root tag: `field`
- Field references: 4
- Sample fields: `company_id`, `shipping_weight`, `weight`, `weight_uom_name`
- XPath or positional patches: 0

### `view_move_line_tree_detailed_delivery`
- Name: stock.move.line.list.detailed
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_move_line_tree_detailed`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `carrier_id`, `destination_country_code`
- XPath or positional patches: 1

### `view_picking_withweight_internal_move_form`
- Name: stock.picking_withweight.internal.move.form.view
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_move_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `weight`
- XPath or positional patches: 1

### `view_picking_withcarrier_out_form`
- Name: delivery.stock.picking_withcarrier.form.view
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `data`
- Field references: 8
- Sample fields: `carrier_id`, `carrier_tracking_ref`, `delivery_type`, `integration_level`, `is_return_picking`, `shipping_weight`, `weight`, `weight_uom_name`
- Buttons: `cancel_shipment`, `open_website_url`, `print_return_label`, `send_to_shipper`
- XPath or positional patches: 5

### `view_delivery_carrier_form_inherit_stock_delivery`
- Name: delivery.carrier.form
- Model: `delivery.carrier`
- Type: inferred from arch
- Inherits: `delivery.view_delivery_carrier_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `route_ids`
- XPath or positional patches: 1

## Actions

- `act_delivery_trackers_url`: `act_window` Display tracking links

## Menus

- `menu_delivery_zip_prefix`: unnamed
- `menu_action_delivery_carrier_form`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/stock_delivery/Views]]

