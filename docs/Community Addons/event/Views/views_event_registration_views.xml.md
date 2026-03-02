<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_registration_views.xml

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Source file: `views/event_registration_views.xml`
- Views: 8
- Actions: 6
- Menus: 1
- Rules: 0

## View records

### `event_registration_view_search_event_specific`
- Name: event.registration.view.search.event.specific
- Model: `event.registration`
- Type: inferred from arch
- Inherits: `view_registration_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `view_registration_search`
- Name: event.registration.search
- Model: `event.registration`
- Type: inferred from arch
- Root tag: `search`
- Field references: 8
- Sample fields: `company_id`, `event_id`, `event_organizer_id`, `event_ticket_id`, `event_user_id`, `id`, `name`, `partner_id`
- XPath or positional patches: 0

### `view_event_registration_graph`
- Name: event.registration.graph
- Model: `event.registration`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `event_id`
- XPath or positional patches: 0

### `view_event_registration_pivot`
- Name: event.registration.pivot
- Model: `event.registration`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 1
- Sample fields: `event_id`
- XPath or positional patches: 0

### `view_event_registration_calendar`
- Name: event.registration.calendar
- Model: `event.registration`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 3
- Sample fields: `event_id`, `name`, `registration_properties`
- XPath or positional patches: 0

### `event_registration_view_kanban`
- Name: event.registration.kanban
- Model: `event.registration`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `active`, `barcode`, `company_name`, `event_id`, `event_slot_id`, `event_ticket_id`, `name`, `registration_properties`, `state`
- XPath or positional patches: 0

### `view_event_registration_form`
- Name: event.registration.form
- Model: `event.registration`
- Type: inferred from arch
- Root tag: `form`
- Field references: 22
- Sample fields: `active`, `barcode`, `company_name`, `create_date`, `date_closed`, `email`, `event_id`, `event_slot_id`, `event_ticket_id`, `name`, and 12 more
- Buttons: `action_cancel`, `action_confirm`, `action_send_badge_email`, `action_set_done`
- XPath or positional patches: 0

### `view_event_registration_tree`
- Name: event.registration.list
- Model: `event.registration`
- Type: inferred from arch
- Root tag: `list`
- Field references: 16
- Sample fields: `active`, `activity_exception_decoration`, `activity_ids`, `barcode`, `company_id`, `company_name`, `create_date`, `email`, `event_id`, `event_slot_id`, and 6 more
- Buttons: `action_cancel`, `action_confirm`, `action_set_done`
- XPath or positional patches: 0

## Actions

- `event_registration_action_stats_from_event`: `act_window` Registration statistics
- `action_registration`: `act_window` Attendees
- `event_registration_action_tree`: `act_window` Event registrations
- `event_registration_action`: `act_window` Attendees
- `event_registration_action_kanban`: `act_window` Attendees
- `act_event_registration_from_event`: `act_window` Attendees

## Menus

- `menu_action_registration`: Attendees

## Navigation

- **Parent:** [[docs/Community Addons/event/Views]]

<!-- GENERATED:VIEWFILE -->
