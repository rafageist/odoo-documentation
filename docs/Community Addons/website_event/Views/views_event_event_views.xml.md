<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_event_views.xml

- Module: [[docs/Community Addons/website_event/website_event|website_event]]
- Scope: Community Addons
- Source file: `views/event_event_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_event_view_search`
- Name: event.event.search.inherit.website
- Model: `event.event`
- Type: inferred from arch
- Inherits: `event.view_event_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `event_event_view_list`
- Name: event.event.view.list.inherit.website
- Model: `event.event`
- Type: inferred from arch
- Inherits: `event.view_event_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `company_id`, `website_id`
- XPath or positional patches: 0

### `event_event_view_form`
- Name: event.event.view.form.inherit.website
- Model: `event.event`
- Type: inferred from arch
- Inherits: `event.view_event_form`
- Root tag: `xpath`
- Field references: 11
- Sample fields: `community_menu`, `event_register_url`, `introduction_menu`, `is_published`, `register_menu`, `tag_ids`, `website_id`, `website_menu`, `website_published`, `website_url`, and 1 more
- Buttons: `website_publish_button`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Community Addons/website_event/Views]]

<!-- GENERATED:VIEWFILE -->
