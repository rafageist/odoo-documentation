<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_registration_views.xml

- Module: [[docs/Community Addons/website_event/website_event|website_event]]
- Scope: Community Addons
- Source file: `views/event_registration_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `event_registration_view_search`
- Name: event.registration.view.search.inherit.online
- Model: `event.registration`
- Type: inferred from arch
- Inherits: `event.view_registration_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `partner_id`, `registration_answer_ids`
- XPath or positional patches: 0

### `event_registration_view_kanban`
- Name: event.registration.kanban.inherit.online
- Model: `event.registration`
- Type: inferred from arch
- Inherits: `event.event_registration_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `registration_answer_choice_ids`
- XPath or positional patches: 1

### `event_registration_view_tree`
- Name: event.registration.view.list.inherit.online
- Model: `event.registration`
- Type: inferred from arch
- Inherits: `event.view_event_registration_tree`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `registration_answer_ids`, `state`, `visitor_id`
- XPath or positional patches: 1

### `event_registration_view_form`
- Name: event.registration.view.form.inherit.online
- Model: `event.registration`
- Type: inferred from arch
- Inherits: `event.view_event_registration_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `visitor_id`
- XPath or positional patches: 1

## Actions

- `event_registration_action_from_visitor`: `act_window` Registrations

## Navigation

- **Parent:** [[docs/Community Addons/website_event/Views]]

<!-- GENERATED:VIEWFILE -->
