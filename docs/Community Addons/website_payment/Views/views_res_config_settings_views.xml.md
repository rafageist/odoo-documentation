<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/website_payment/website_payment|website_payment]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.website
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `website.res_config_settings_view_form`
- Root tag: `setting`
- Field references: 2
- Sample fields: `active_provider_id`, `onboarding_payment_module`
- Buttons: `%(payment.action_payment_provider)d`, `action_view_active_provider`, `action_w_payment_start_payment_onboarding`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/website_payment/Views]]

<!-- GENERATED:VIEWFILE -->
