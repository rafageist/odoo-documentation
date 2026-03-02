<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_tag_views.xml

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Source file: `views/event_tag_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `event_tag_view_form`
- Name: event.tag.view.form
- Model: `event.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `category_id`, `color`, `name`
- XPath or positional patches: 0

### `event_tag_view_tree`
- Name: event.tag.view.list
- Model: `event.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `category_id`, `color`, `name`, `sequence`
- XPath or positional patches: 0

### `event_tag_category_view_form`
- Name: event.tag.category.view.form
- Model: `event.tag.category`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `color`, `name`, `sequence`, `tag_ids`
- XPath or positional patches: 0

### `event_tag_category_view_tree`
- Name: event.tag.category.view.list
- Model: `event.tag.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `name`, `sequence`, `tag_ids`
- XPath or positional patches: 0

## Actions

- `event_tag_category_action_tree`: `act_window` Event Tags Categories

## Menus

- `menu_event_category`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/event/Views]]

<!-- GENERATED:VIEWFILE -->
