<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/purchase/purchase|purchase]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `res_config_settings_view_form_purchase`
- Name: res.config.settings.view.form.inherit.purchase
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 13
- Sample fields: `company_currency_id`, `group_product_variant`, `group_send_reminder`, `group_uom`, `group_warning_purchase`, `lock_confirmed_po`, `module_account_3way_match`, `module_purchase_product_matrix`, `module_purchase_requisition`, `po_double_validation`, and 3 more
- Buttons: `%(product.attribute_action)d`, `%(uom.product_uom_form_action)d`
- XPath or positional patches: 1

## Actions

- `action_purchase_configuration`: `act_window` Settings

## Menus

- `menu_purchase_general_settings`: Settings

## Navigation

- **Parent:** [[docs/Community Addons/purchase/Views]]

<!-- GENERATED:VIEWFILE -->
