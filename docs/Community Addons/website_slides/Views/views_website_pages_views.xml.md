---
tags: [odoo, community, generated, views]
---

# views/website_pages_views.xml

- Module: [[docs/Community Addons/website_slides/website_slides|website_slides]]
- Scope: Community Addons
- Source file: `views/website_pages_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `slide_channel_pages_kanban_view`
- Name: Course Pages Kanban
- Model: `slide.channel`
- Type: inferred from arch
- Inherits: `slide_channel_view_kanban`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `is_published`, `website_id`, `website_url`
- XPath or positional patches: 4

### `slide_channel_pages_tree_view`
- Name: Course Pages List
- Model: `slide.channel`
- Type: inferred from arch
- Inherits: `slide_channel_view_tree`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `is_published`, `is_seo_optimized`, `name`, `website_id`, `website_url`
- XPath or positional patches: 2

## Actions

- `action_slide_channel_pages_list`: `act_window` Course Pages

## Menus

- `menu_slide_channel_pages`: Courses

## Navigation

- **Parent:** [[docs/Community Addons/website_slides/Views]]

