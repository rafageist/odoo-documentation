---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.point_of_sale
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 88
- Sample fields: `account_default_pos_receivable_account_id`, `barcode_nomenclature_id`, `group_cash_rounding`, `is_kiosk_mode`, `module_loyalty`, `module_pos_adyen`, `module_pos_mercado_pago`, `module_pos_pine_labs`, `module_pos_pricer`, `module_pos_qfpay`, and 78 more
- Buttons: `%(account.action_account_fiscal_position_form)d`, `%(account.action_tax_form)d`, `%(account.rounding_list_action)d`, `%(action_payment_methods_tree)d`, `%(action_pos_preset_form)d`, `%(point_of_sale.action_pos_config_tree)d`, `%(point_of_sale.action_pos_note_model)d`, `%(point_of_sale.action_pos_printer_form)d`, `%(product.product_pricelist_action2)d`, `%(product_pos_category_action)d`, and 4 more
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

