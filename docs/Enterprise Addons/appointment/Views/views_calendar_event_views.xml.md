<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/calendar_event_views.xml

- Module: [[docs/Enterprise Addons/appointment/appointment|appointment]]
- Scope: Enterprise Addons
- Source file: `views/calendar_event_views.xml`
- Views: 13
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `calendar_event_view_pivot`
- Name: calendar.event.view.pivot
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `categ_ids`, `name`, `start`, `user_id`
- XPath or positional patches: 0

### `calendar_event_view_graph`
- Name: calendar.event.view.graph
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `res_id`, `start`
- XPath or positional patches: 0

### `calendar_event_view_calendar_booking_resource`
- Name: calendar.event.view.calendar.booking.resource.appointment
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `appointment.calendar_event_view_calendar`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `appointment_resource_ids`
- XPath or positional patches: 2

### `calendar_event_view_calendar`
- Name: calendar.event.view.calendar.appointment
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `calendar.view_calendar_event_calendar`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `appointment_resource_ids`, `appointment_status`, `res_model_name`
- XPath or positional patches: 4

### `calendar_event_view_gantt_booking_user`
- Name: calendar.event.view.gantt.meeting.user
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `appointment.calendar_event_view_gantt_booking_resource`
- Root tag: `gantt`
- Field references: 0
- XPath or positional patches: 1

### `calendar_event_view_gantt_booking_resource`
- Name: calendar.event.view.gantt.booking.resource
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 14
- Sample fields: `active`, `appointment_booker_id`, `appointment_resource_ids`, `appointment_type_id`, `appointment_type_manage_capacity`, `appointment_type_schedule_based_on`, `booking_line_ids`, `description`, `partner_id`, `partner_ids`, and 4 more
- XPath or positional patches: 0

### `calendar_event_view_gantt_kanban_popover`
- Name: calendar.event.view.gantt.kanban.popover
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `appointment_status`, `description`, `location`, `start`, `stop`, `total_capacity_reserved`, `videocall_location`
- XPath or positional patches: 0

### `calendar_event_view_form_gantt_booking`
- Name: calendar.event.view.form.gantt.booking
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `calendar.view_calendar_event_form_quick_create`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `appointment_status`, `appointment_type_id`, `name`, `resource_ids`, `total_capacity_reserved`, `unavailable_partner_ids`, `unavailable_resource_ids`
- XPath or positional patches: 6

### `calendar_event_view_tree_booking`
- Name: calendar.event.view.list.booking
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `active`, `appointment_resource_ids`, `appointment_status`, `appointment_type_id`, `attendee_ids`, `name`, `start`, `stop`, `total_capacity_reserved`, `total_capacity_used`
- XPath or positional patches: 0

### `calendar_event_view_search_booking`
- Name: calendar.event.view.search.inherit.appointment.booking
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `calendar.view_calendar_event_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `appointment_status`
- XPath or positional patches: 9

### `calendar_event_view_search`
- Name: calendar.event.view.search.inherit.appointment
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `calendar.view_calendar_event_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `appointment_type_id`
- XPath or positional patches: 2

### `calendar_event_view_tree`
- Name: calendar.event.view.list.inherit.appointment
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `calendar.view_calendar_event_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `appointment_resource_ids`, `appointment_type_id`
- XPath or positional patches: 1

### `calendar_event_view_form`
- Name: calendar.event.view.form.inherit.appointment
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `calendar.view_calendar_event_form`
- Root tag: `header`
- Field references: 17
- Sample fields: `appointment_answer_input_ids`, `appointment_resource_id`, `appointment_status`, `appointment_type_id`, `appointment_type_manage_capacity`, `appointment_type_schedule_based_on`, `appointment_user_id`, `booking_line_ids`, `capacity_reserved`, `capacity_used`, and 7 more
- Buttons: `action_set_appointment_attended`, `action_set_appointment_booked`, `action_set_appointment_cancelled`, `action_set_appointment_no_show`
- XPath or positional patches: 3

## Actions

- `calendar_event_action_appointment_reporting`: `act_window` Appointments
- `calendar_event_action_report_all`: `act_window` All Appointments
- `calendar_event_action_all_users_appointments`: `server` Staff Bookings
- `calendar_event_action_all_resources_bookings`: `server` Resource Bookings
- `calendar_event_action_view_bookings_users`: `act_window` Staff Bookings
- `calendar_event_action_view_bookings_resources`: `act_window` Resource Bookings

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment/Views]]

<!-- GENERATED:VIEWFILE -->
