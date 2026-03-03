---
tags: [odoo, community, generated, views]
---

# views/website_controller_pages_views.xml

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Source file: `views/website_controller_pages_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `website_controller_pages_search_view`
- Name: website.controller.page.search
- Model: `website.controller.page`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `model`
- XPath or positional patches: 0

### `website_controller_pages_kanban_view`
- Name: website.controller.page.kanban
- Model: `website.controller.page`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `name`, `url_demo`, `website_id`, `website_published`
- XPath or positional patches: 0

### `website_controller_pages_tree_view`
- Name: website.controller.page.list
- Model: `website.controller.page`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `is_published`, `name`, `url_demo`, `website_id`
- XPath or positional patches: 0

### `website_controller_pages_form_view`
- Name: website.controller.page.form
- Model: `website.controller.page`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `default_layout`, `menu_ids`, `model`, `model_id`, `name`, `name_slugified`, `record_domain`, `view_id`, `website_id`, `website_published`
- XPath or positional patches: 0

## Actions

- `action_website_controller_pages_list`: `act_window` Website Model Pages

## Menus

- `menu_website_controller_pages_list`: Model Pages

## Navigation

- **Parent:** [[docs/Community Addons/website/Views]]

