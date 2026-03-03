---
tags: [odoo, community, generated, views]
---

# views/website_pages_views.xml

- Module: [[docs/Community Addons/website_event/website_event|website_event]]
- Scope: Community Addons
- Source file: `views/website_pages_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `event_pages_kanban_view`
- Name: Event Pages Kanban
- Model: `event.event`
- Type: inferred from arch
- Inherits: `event.view_event_kanban`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `is_published`, `website_id`, `website_url`
- XPath or positional patches: 4

### `event_pages_tree_view`
- Name: Event Pages List
- Model: `event.event`
- Type: inferred from arch
- Inherits: `event.view_event_tree`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `address_id`, `date_end`, `is_published`, `is_seo_optimized`, `name`, `seats_used`, `stage_id`, `website_id`, `website_url`
- XPath or positional patches: 1

## Actions

- `action_event_pages_list`: `act_window` Event Pages

## Menus

- `menu_event_pages`: Events

## Navigation

- **Parent:** [[docs/Community Addons/website_event/Views]]

