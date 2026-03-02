<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_booth_views.xml

- Module: [[docs/Community Addons/event_booth/event_booth|event_booth]]
- Scope: Community Addons
- Source file: `views/event_booth_views.xml`
- Views: 11
- Actions: 5
- Menus: 0
- Rules: 0

## View records

### `event_booth_view_pivot`
- Name: event.booth.view.pivot
- Model: `event.booth`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 1
- Sample fields: `booth_category_id`
- XPath or positional patches: 0

### `event_booth_view_graph`
- Name: event.booth.view.graph
- Model: `event.booth`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `booth_category_id`
- XPath or positional patches: 0

### `event_booth_view_search`
- Name: event.booth.view.search
- Model: `event.booth`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `contact_email`, `contact_name`, `event_id`, `name`
- XPath or positional patches: 0

### `event_booth_view_form_quick_create`
- Name: event.booth.view.form.quick_create
- Model: `event.booth`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `booth_category_id`, `name`
- XPath or positional patches: 0

### `event_booth_view_kanban`
- Name: event.booth.view.kanban
- Model: `event.booth`
- Type: inferred from arch
- Inherits: `event_booth_view_kanban_from_event`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `event_id`
- XPath or positional patches: 1

### `event_booth_view_kanban_from_event`
- Name: event.booth.view.kanban
- Model: `event.booth`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `activity_ids`, `booth_category_id`, `name`
- XPath or positional patches: 0

### `event_booth_view_tree`
- Name: event.booth.view.list
- Model: `event.booth`
- Type: inferred from arch
- Inherits: `event_booth_view_tree_from_event`
- Root tag: `field`
- Field references: 2
- Sample fields: `event_id`, `name`
- XPath or positional patches: 0

### `event_booth_view_tree_from_event`
- Name: event.booth.view.list.from.event
- Model: `event.booth`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `booth_category_id`, `contact_email`, `contact_name`, `contact_phone`, `name`, `partner_id`, `state`
- XPath or positional patches: 0

### `event_booth_view_form_simple_from_event`
- Name: event.booth.view.form.simple.from.event
- Model: `event.booth`
- Type: inferred from arch
- Inherits: `event_booth_view_form_from_event`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `event_booth_view_form`
- Name: event.booth.view.form
- Model: `event.booth`
- Type: inferred from arch
- Inherits: `event_booth_view_form_from_event`
- Root tag: `field`
- Field references: 2
- Sample fields: `booth_category_id`, `event_id`
- XPath or positional patches: 0

### `event_booth_view_form_from_event`
- Name: event.booth.view.form.from.event
- Model: `event.booth`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `booth_category_id`, `contact_email`, `contact_name`, `contact_phone`, `name`, `partner_id`, `state`
- XPath or positional patches: 0

## Actions

- `event_booth_action_from_event_view_form`: `view`
- `event_booth_action_from_event_view_tree`: `view`
- `event_booth_action_from_event_view_kanban`: `view`
- `event_booth_action_from_event`: `act_window` Booths
- `event_booth_action`: `act_window` Booths

## Navigation

- **Parent:** [[docs/Community Addons/event_booth/Views]]

<!-- GENERATED:VIEWFILE -->
