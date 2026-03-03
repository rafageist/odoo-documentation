---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.stock
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 36
- Sample fields: `annual_inventory_day`, `annual_inventory_month`, `barcode_separator`, `group_lot_on_delivery_slip`, `group_product_variant`, `group_stock_adv_location`, `group_stock_lot_print_gs1`, `group_stock_multi_locations`, `group_stock_production_lot`, `group_stock_reception_report`, and 26 more
- Buttons: `%(product.attribute_action)d`, `%(stock.action_location_form)d`, `%(stock.action_warehouse_form)d`, `%(uom.product_uom_form_action)d`
- XPath or positional patches: 1

## Actions

- `action_stock_config_settings`: `act_window` Settings

## Menus

- `menu_stock_general_settings`: Settings
- `menu_stock_config_settings`: Configuration

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

