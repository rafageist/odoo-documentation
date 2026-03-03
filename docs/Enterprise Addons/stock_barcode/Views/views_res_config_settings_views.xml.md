---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.stock.barcode
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `stock.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `barcode_max_time_between_keys_in_ms`, `barcode_nomenclature_id`, `barcode_rfid_batch_time`, `barcode_separator_regex`, `show_barcode_nomenclature`, `stock_barcode_demo_active`, `stock_barcode_mute_sound_notifications`
- Buttons: `%(stock_barcode.product_action_barcodes)d`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode/Views]]

