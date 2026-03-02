<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/base_setup/base_setup|base_setup]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.base.setup
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 23
- Sample fields: `active_user_count`, `company_count`, `company_id`, `company_informations`, `company_name`, `external_report_layout_id`, `is_root_company`, `language_count`, `module_account_inter_company_rules`, `module_auth_ldap`, and 13 more
- Buttons: `%(base.action_apikeys_admin)d`, `%(base.action_res_company_form)d`, `%(base.action_res_users)d`, `%(base.action_view_base_language_install)d`, `%(base.res_lang_act_window)d`, `%(web.action_base_document_layout_configurator)d`, `%(web.action_report_externalpreview)d`, `edit_external_header`, `open_company`, `open_new_user_default_groups`
- XPath or positional patches: 1

## Actions

- `action_general_configuration`: `act_window` Settings

## Menus

- `menu_config`: General Settings

## Navigation

- **Parent:** [[docs/Community Addons/base_setup/Views]]

<!-- GENERATED:VIEWFILE -->
