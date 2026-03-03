---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/delivery_sendcloud/delivery_sendcloud|delivery_sendcloud]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form_stock`
- Name: res.config.settings.view.form.stock
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `stock.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `%(delivery.action_delivery_carrier_form)d`
- XPath or positional patches: 1

### `res_config_settings_view_form_sale`
- Name: res.config.settings.view.form.sale
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `sale.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `%(delivery.action_delivery_carrier_form)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/delivery_sendcloud/Views]]

