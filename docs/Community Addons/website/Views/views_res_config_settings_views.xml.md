---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 2
- Actions: 1
- Menus: 5
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.website
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 25
- Sample fields: `auth_signup_uninvited`, `cdn_activated`, `cdn_filters`, `cdn_url`, `favicon`, `google_analytics_key`, `google_search_console`, `has_default_share_image`, `has_google_analytics`, `has_google_search_console`, and 15 more
- Buttons: `%(base.action_view_base_language_install)d`, `%(website.backend_dashboard)d`, `action_open_blocked_third_party_domains`, `action_open_robots`, `action_open_template_user`, `action_website_create_new`
- XPath or positional patches: 1

### `res_config_settings_view_form_inherit_auth_signup`
- Name: res.config.settings.view.form.inherit.website
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `auth_signup.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `action_website_configuration`: `act_window` Settings

## Menus

- `menu_website_menu_list`: Menus
- `menu_website_websites_list`: Websites
- `menu_website_add_features`: unnamed
- `menu_website_website_settings`: Settings
- `menu_website_global_configuration`: Configuration

## Navigation

- **Parent:** [[docs/Community Addons/website/Views]]

