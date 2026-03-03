---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/website_sale_renting/website_sale_renting|website_sale_renting]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form_inherit_website`
- Name: res.config.settings.view.form.inherit.website
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `website.res_config_settings_view_form`
- Root tag: `setting`
- Field references: 1
- Sample fields: `tz`
- XPath or positional patches: 1

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.website.sale.renting
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `sale_renting.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `renting_forbidden_fri`, `renting_forbidden_mon`, `renting_forbidden_sat`, `renting_forbidden_sun`, `renting_forbidden_thu`, `renting_forbidden_tue`, `renting_forbidden_wed`, `renting_minimal_time_duration`, `renting_minimal_time_unit`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_sale_renting/Views]]

