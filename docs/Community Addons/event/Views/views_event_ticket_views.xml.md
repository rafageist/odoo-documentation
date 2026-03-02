<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_ticket_views.xml

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Source file: `views/event_ticket_views.xml`
- Views: 9
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_event_ticket_form_view`
- Name: event.event.ticket.view.form
- Model: `event.event.ticket`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `end_sale_datetime`, `event_id`, `is_expired`, `name`, `seats_available`, `seats_limited`, `seats_max`, `seats_reserved`, `seats_used`, `start_sale_datetime`
- XPath or positional patches: 0

### `event_event_ticket_view_tree`
- Name: event.event.ticket.view.list
- Model: `event.event.ticket`
- Type: inferred from arch
- Inherits: `event_event_ticket_view_tree_from_event`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `event_id`, `name`
- XPath or positional patches: 1

### `event_event_ticket_view_kanban_from_event`
- Name: event.event.ticket.view.kanban.from.event
- Model: `event.event.ticket`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `name`, `seats_reserved`
- XPath or positional patches: 0

### `event_event_ticket_view_form_from_event`
- Name: event.event.ticket.view.form.from.event
- Model: `event.event.ticket`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `description`, `end_sale_datetime`, `name`, `seats_max`, `seats_reserved`, `start_sale_datetime`
- XPath or positional patches: 0

### `event_event_ticket_view_tree_from_event`
- Name: event.event.ticket.view.list.from.event
- Model: `event.event.ticket`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `color`, `description`, `end_sale_datetime`, `limit_max_per_order`, `name`, `seats_max`, `seats_taken`, `sequence`, `start_sale_datetime`
- XPath or positional patches: 0

### `event_type_ticket_view_form`
- Name: event.type.ticket.view.form
- Model: `event.type.ticket`
- Type: inferred from arch
- Inherits: `event_type_ticket_view_form_from_type`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `event_type_id`
- XPath or positional patches: 1

### `event_type_ticket_view_tree`
- Name: event.type.ticket.view.list
- Model: `event.type.ticket`
- Type: inferred from arch
- Inherits: `event_type_ticket_view_tree_from_type`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `event_type_id`
- XPath or positional patches: 2

### `event_type_ticket_view_form_from_type`
- Name: event.type.ticket.view.form.from.type
- Model: `event.type.ticket`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `description`, `name`, `seats_limited`, `seats_max`
- XPath or positional patches: 0

### `event_type_ticket_view_tree_from_type`
- Name: event.type.ticket.view.list.from.type
- Model: `event.type.ticket`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `description`, `name`, `seats_limited`, `seats_max`, `sequence`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/event/Views]]

<!-- GENERATED:VIEWFILE -->
