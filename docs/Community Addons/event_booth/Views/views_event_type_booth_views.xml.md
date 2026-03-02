<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_type_booth_views.xml

- Module: [[docs/Community Addons/event_booth/event_booth|event_booth]]
- Scope: Community Addons
- Source file: `views/event_type_booth_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `event_type_booth_view_search`
- Name: event.type.booth.view.search
- Model: `event.type.booth`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `event_type_booth_view_tree`
- Name: event.type.booth.view.list
- Model: `event.type.booth`
- Type: inferred from arch
- Inherits: `event_type_booth_view_tree_from_type`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `event_type_id`
- XPath or positional patches: 1

### `event_type_booth_view_tree_from_type`
- Name: event.type.booth.view.list.from.type
- Model: `event.type.booth`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `booth_category_id`, `name`
- XPath or positional patches: 0

### `event_type_booth_view_form`
- Name: event.type.booth.view.form
- Model: `event.type.booth`
- Type: inferred from arch
- Inherits: `event_type_booth_view_form_from_type`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `event_type_id`
- XPath or positional patches: 1

### `event_type_booth_view_form_from_type`
- Name: event.type.booth.view.form.from.type
- Model: `event.type.booth`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `booth_category_id`, `name`
- XPath or positional patches: 0

## Actions

- `event_type_booth_action`: `act_window` Event Type Booths

## Navigation

- **Parent:** [[docs/Community Addons/event_booth/Views]]

<!-- GENERATED:VIEWFILE -->
