---
tags: [odoo, community, generated, views]
---

# views/event_booth_category_views.xml

- Module: [[docs/Community Addons/website_event_booth_exhibitor/website_event_booth_exhibitor|website_event_booth_exhibitor]]
- Scope: Community Addons
- Source file: `views/event_booth_category_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_booth_category_view_search`
- Name: event.booth.category.view.search.inherit.website.event.booth.exhibitor
- Model: `event.booth.category`
- Type: inferred from arch
- Inherits: `event_booth.event_booth_category_view_search`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `exhibitor_type`, `sponsor_type_id`, `use_sponsor`
- XPath or positional patches: 1

### `event_booth_category_view_tree`
- Name: event.booth.category.view.list.inherit.website.event.booth.exhibitor
- Model: `event.booth.category`
- Type: inferred from arch
- Inherits: `event_booth.event_booth_category_view_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `exhibitor_type`, `name`, `sponsor_type_id`, `use_sponsor`
- XPath or positional patches: 0

### `event_booth_category_view_form`
- Name: event.booth.category.view.form.inherit.website.event.booth.exhibitor
- Model: `event.booth.category`
- Type: inferred from arch
- Inherits: `event_booth.event_booth_category_view_form`
- Root tag: `group`
- Field references: 3
- Sample fields: `exhibitor_type`, `sponsor_type_id`, `use_sponsor`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_event_booth_exhibitor/Views]]

