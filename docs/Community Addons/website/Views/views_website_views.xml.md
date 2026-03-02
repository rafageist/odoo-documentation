<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/website_views.xml

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Source file: `views/website_views.xml`
- Views: 11
- Actions: 14
- Menus: 14
- Rules: 0

## View records

### `theme_view_form_preview`
- Name: website.form
- Model: `ir.module.module`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `url`
- XPath or positional patches: 0

### `theme_view_search`
- Name: Themes Search
- Model: `ir.module.module`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `category_id`, `name`
- XPath or positional patches: 0

### `theme_view_kanban`
- Name: Themes Kanban
- Model: `ir.module.module`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `category_id`, `display_name`, `icon`, `image_ids`, `is_installed_on_current_website`, `name`, `state`, `summary`, `url`
- Buttons: `button_choose_theme`, `button_refresh_theme`, `button_remove_theme`
- XPath or positional patches: 0

### `view_arch_only`
- Name: website.ir_ui_view.arch_only
- Model: `ir.ui.view`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `arch`
- XPath or positional patches: 0

### `reset_view_arch_wizard_view`
- Name: unnamed
- Model: `reset.view.arch.wizard`
- Type: inferred from arch
- Inherits: `base.reset_view_arch_wizard_view`
- Root tag: `field`
- Field references: 1
- Sample fields: `compare_view_id`
- XPath or positional patches: 0

### `menu_search`
- Name: website.menu.search
- Model: `website.menu`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `name`, `url`, `website_id`
- XPath or positional patches: 0

### `menu_tree`
- Name: website.menu.list
- Model: `website.menu`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `group_ids`, `is_mega_menu`, `name`, `new_window`, `parent_id`, `sequence`, `url`, `website_id`
- XPath or positional patches: 0

### `website_menus_form_view`
- Name: website.menu.form
- Model: `website.menu`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `child_id`, `controller_page_id`, `group_ids`, `is_mega_menu`, `name`, `new_window`, `page_id`, `parent_id`, `sequence`, `url`, and 1 more
- XPath or positional patches: 0

### `view_website_tree`
- Name: website.list
- Model: `website`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `company_id`, `default_lang_id`, `domain`, `name`, `sequence`, `theme_id`
- XPath or positional patches: 0

### `view_website_form_view_themes_modal`
- Name: website.modal.form
- Model: `website`
- Type: inferred from arch
- Inherits: `website.view_website_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `create_and_redirect_configurator`
- XPath or positional patches: 3

### `view_website_form`
- Name: website.form
- Model: `website`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `company_id`, `custom_code_footer`, `custom_code_head`, `default_lang_id`, `domain`, `language_count`, `language_ids`, `logo`, `name`
- XPath or positional patches: 0

## Actions

- `website_configurator_todo`: `todo` Start Website Configurator
- `action_open_website_configurator`: `client` Open Website Configurator
- `website_configurator`: `client` Website Configurator
- `theme_install_kanban_action`: `act_window` Pick a Theme
- `base.open_module_tree`: `act_window`
- `ir_actions_server_website_analytics`: `server` Website: Analytics
- `ir_actions_server_website_dashboard`: `server` Website: Dashboard
- `open_custom_menu`: `client` Open Custom Menu
- `website_preview`: `client` Website Preview
- `backend_dashboard`: `client` Analytics
- `action_website_menu`: `act_window` Website Menu
- `action_website_list`: `act_window` Websites
- `action_website_view_hierarchy`: `client` View Hierarchy
- `action_website_add_features`: `act_window` Apps

## Menus

- `menu_website_technical_pages`: Technical Pages
- `menu_website_analytics`: Analytics
- `menu_website_dashboard`: eCommerce
- `menu_reporting`: Reporting
- `custom_menu_edit_menu`: Edit Menu
- `menu_ace_editor`: HTML / CSS Editor
- `menu_optimize_seo`: Optimize SEO
- `menu_page_properties`: Properties
- `menu_current_page`: This page
- `menu_content`: Content
- `menu_edit_menu`: Menu Editor
- `menu_website_preview`: Homepage
- `menu_site`: Site
- `menu_website_configuration`: Website

## Navigation

- **Parent:** [[docs/Community Addons/website/Views]]

<!-- GENERATED:VIEWFILE -->
