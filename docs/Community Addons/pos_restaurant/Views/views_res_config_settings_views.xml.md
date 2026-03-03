---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.pos_restaurant
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `point_of_sale.res_config_settings_view_form`
- Root tag: `div`
- Field references: 5
- Sample fields: `pos_default_screen`, `pos_floor_ids`, `pos_iface_printbill`, `pos_iface_splitbill`, `pos_set_tip_after_payment`
- Buttons: `%(pos_restaurant.action_restaurant_floor_form)d`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Community Addons/pos_restaurant/Views]]

