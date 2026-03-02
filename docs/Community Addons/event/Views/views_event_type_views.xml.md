<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_type_views.xml

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Source file: `views/event_type_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `event_type_view_search`
- Name: event.type.search
- Model: `event.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_event_type_tree`
- Name: event.type.list
- Model: `event.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `name`, `sequence`
- XPath or positional patches: 0

### `view_event_type_form`
- Name: event.type.form
- Model: `event.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `answer_ids`, `default_timezone`, `event_type_mail_ids`, `event_type_ticket_ids`, `has_seats_limitation`, `interval_nbr`, `interval_type`, `interval_unit`, `is_default`, `is_mandatory_answer`, and 11 more
- XPath or positional patches: 0

## Actions

- `action_event_type`: `act_window` Event Templates

## Menus

- `menu_event_type`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/event/Views]]

<!-- GENERATED:VIEWFILE -->
