---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/pos_urban_piper/pos_urban_piper|pos_urban_piper]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form_pos_urban_piper`
- Name: res.config.settings.view.form.inherit.pos_urban_piper
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `point_of_sale.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `pos_urbanpiper_delivery_provider_ids`, `pos_urbanpiper_fiscal_position_id`, `pos_urbanpiper_last_sync_date`, `pos_urbanpiper_pricelist_id`, `pos_urbanpiper_store_identifier`, `urbanpiper_apikey`, `urbanpiper_username`
- Buttons: `action_flush_and_sync_menu`, `action_refresh_webhooks`, `open_test_order_wizard`, `urbanpiper_create_store`, `urbanpiper_sync_menu`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_urban_piper/Views]]

