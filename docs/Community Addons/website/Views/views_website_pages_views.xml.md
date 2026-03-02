<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/website_pages_views.xml

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Source file: `views/website_pages_views.xml`
- Views: 8
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_view_tree_inherit_website`
- Name: unnamed
- Model: `ir.ui.view`
- Type: inferred from arch
- Inherits: `base.view_view_tree`
- Root tag: `list`
- Field references: 5
- Sample fields: `active`, `key`, `name`, `website_id`, `xml_id`
- XPath or positional patches: 1

### `view_view_form_extend`
- Name: unnamed
- Model: `ir.ui.view`
- Type: inferred from arch
- Inherits: `base.view_view_form`
- Root tag: `field`
- Field references: 10
- Sample fields: `active`, `first_page_id`, `inherit_id`, `key`, `model_id`, `page_ids`, `track`, `visibility`, `visibility_password_display`, `website_id`
- Buttons: `website.action_website_pages_list`, `website.action_website_view_hierarchy`
- XPath or positional patches: 1

### `website_pages_view_search`
- Name: website.page.view.search
- Model: `website.page`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `url`
- XPath or positional patches: 0

### `website_pages_kanban_view`
- Name: website.page.kanban
- Model: `website.page`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `is_homepage`, `is_in_menu`, `is_published`, `is_seo_optimized`, `name`, `website_id`, `website_url`
- Buttons: `action_page_debug_view`
- XPath or positional patches: 0

### `website_pages_tree_view`
- Name: website.page.list
- Model: `website.page`
- Type: inferred from arch
- Root tag: `list`
- Field references: 15
- Sample fields: `create_date`, `create_uid`, `is_homepage`, `is_in_menu`, `is_published`, `is_seo_optimized`, `name`, `track`, `view_write_date`, `view_write_uid`, and 5 more
- Buttons: `action_page_debug_view`
- XPath or positional patches: 0

### `website_page_properties_view_form`
- Name: website.page.properties.form.view
- Model: `website.page.properties`
- Type: inferred from arch
- Inherits: `website_page_properties_base_view_form`
- Root tag: `xpath`
- Field references: 11
- Sample fields: `date_publish`, `group_ids`, `is_new_page_template`, `name`, `redirect_old_url`, `redirect_type`, `url`, `visibility`, `visibility_password_display`, `website_id`, and 1 more
- XPath or positional patches: 3

### `website_page_properties_base_view_form`
- Name: website.page.properties.base.form.view
- Model: `website.page.properties.base`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `is_homepage`, `is_in_menu`, `is_published`
- Buttons: `%(website.open_custom_menu)d`
- XPath or positional patches: 0

### `website_pages_form_view`
- Name: website.page.form
- Model: `website.page`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `date_publish`, `is_published`, `menu_ids`, `name`, `track`, `url`, `view_id`, `website_id`, `website_indexed`
- XPath or positional patches: 0

## Actions

- `action_website_pages_list`: `act_window` Website Pages

## Menus

- `menu_website_pages_list`: Pages

## Navigation

- **Parent:** [[docs/Community Addons/website/Views]]

<!-- GENERATED:VIEWFILE -->
