<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.website.sale
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `website_payment.res_config_settings_view_form`
- Root tag: `setting`
- Field references: 22
- Sample fields: `account_on_checkout`, `add_to_cart_action`, `automatic_invoice`, `cart_abandoned_delay`, `confirmation_email_template_id`, `default_invoice_policy`, `ecommerce_access`, `group_gmc_feed`, `group_product_price_comparison`, `group_product_pricelist`, and 12 more
- Buttons: `%(delivery.action_delivery_carrier_form)d`, `%(product.attribute_action)d`, `%(product.product_pricelist_action2)d`, `action_open_abandoned_cart_mail_template`, `action_open_product_feeds`, `action_view_delivery_provider_modules`
- XPath or positional patches: 4

### `res_config_settings_view_form_inherit_sale`
- Name: res.config.settings.view.form.inherit.sale
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `sale.res_config_settings_view_form`
- Root tag: `setting`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Views]]

<!-- GENERATED:VIEWFILE -->
