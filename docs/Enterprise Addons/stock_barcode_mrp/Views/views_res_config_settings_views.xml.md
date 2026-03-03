---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/stock_barcode_mrp/stock_barcode_mrp|stock_barcode_mrp]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.mrp.barcode
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `mrp.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `barcode_nomenclature_id`, `show_barcode_nomenclature`, `stock_barcode_demo_active`
- Buttons: `%(stock_barcode.product_action_barcodes)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode_mrp/Views]]

