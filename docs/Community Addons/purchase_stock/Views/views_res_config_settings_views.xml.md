<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form_stock`
- Name: res.config.settings.view.form.inherit.purchase.stock
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `stock.res_config_settings_view_form`
- Root tag: `div`
- Field references: 1
- Sample fields: `days_to_purchase`
- XPath or positional patches: 1

### `res_config_settings_view_form_purchase`
- Name: res.config.settings.view.form.inherit.purchase
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `purchase.res_config_settings_view_form_purchase`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `is_installed_sale`, `module_stock_dropshipping`, `replenish_on_order`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/purchase_stock/Views]]

<!-- GENERATED:VIEWFILE -->
