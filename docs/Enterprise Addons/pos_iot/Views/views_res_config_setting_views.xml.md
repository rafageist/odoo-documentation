<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_setting_views.xml

- Module: [[docs/Enterprise Addons/pos_iot/pos_iot|pos_iot]]
- Scope: Enterprise Addons
- Source file: `views/res_config_setting_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_view_form_inherit_pos_iot`
- Name: res.config.form.inherit.pos.iot
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `point_of_sale.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `module_pos_iot_ingenico`, `module_pos_iot_six`, `module_pos_iot_worldline`, `pos_iface_cashdrawer`, `pos_iface_display_id`, `pos_iface_printer_id`, `pos_iface_scale_id`, `pos_iface_scanner_ids`
- Buttons: `%(iot.iot_device_action)d`, `open_payment_method_form`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_iot/Views]]

<!-- GENERATED:VIEWFILE -->
