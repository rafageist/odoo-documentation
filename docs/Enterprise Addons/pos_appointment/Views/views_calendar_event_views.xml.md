<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/calendar_event_views.xml

- Module: [[docs/Enterprise Addons/pos_appointment/pos_appointment|pos_appointment]]
- Scope: Enterprise Addons
- Source file: `views/calendar_event_views.xml`
- Views: 6
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `calendar_event_view_graph_pos_appointment`
- Name: calendar.event.view.graph.pos.appointment
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `appointment_status`, `start`
- XPath or positional patches: 0

### `calendar_event_view_kanban`
- Name: calendar.event.view.kanban.pos.appointment
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 11
- Sample fields: `appointment_status`, `appointment_type_id`, `description`, `duration`, `id`, `name`, `phone_number`, `resource_ids`, `start`, `stop`, and 1 more
- XPath or positional patches: 0

### `calendar_event_view_tree`
- Name: calendar.event.view.tree.pos.appointment
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `calendar.view_calendar_event_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `calendar_event_view_calendar`
- Name: calendar.event.view.calendar.pos.appointment
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `appointment.calendar_event_view_calendar`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `calendar_event_view_gantt_booking_resource`
- Name: calendar.event.view.gantt.booking.resource.pos.appointment
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `appointment.calendar_event_view_gantt_booking_resource`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `description`, `duration`, `phone_number`, `resource_ids`, `waiting_list_capacity`
- XPath or positional patches: 2

### `calendar_event_view_form_gantt_booking`
- Name: calendar.event.view.form.gantt.booking
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `answers`, `appointment_status`, `description`, `duration`, `name`, `phone_number`, `resource_ids`, `start`, `stop`, `total_capacity_reserved`, and 1 more
- Buttons: `set_attended`, `set_cancelled`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_appointment/Views]]

<!-- GENERATED:VIEWFILE -->
