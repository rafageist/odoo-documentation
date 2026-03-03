---
tags: [odoo, community, generated, views]
---

# wizard/res_config_settings_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `wizard/res_config_settings_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form_sale_inherit`
- Name: res.config.settings.view.form.inherit.sale
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `account.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `downpayment_account_id`
- XPath or positional patches: 1

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.sale
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 33
- Sample fields: `active_provider_id`, `auth_signup_uninvited`, `automatic_invoice`, `default_invoice_policy`, `group_auto_done_setting`, `group_discount_per_so_line`, `group_product_pricelist`, `group_product_variant`, `group_proforma_sales`, `group_uom`, and 23 more
- Buttons: `%(payment.action_payment_provider)d`, `%(product.attribute_action)d`, `%(product.product_pricelist_action2)d`, `%(uom.product_uom_form_action)d`, `action_sale_start_payment_onboarding`, `action_view_active_provider`
- XPath or positional patches: 1

## Actions

- `action_sale_config_settings`: `act_window` Settings

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

