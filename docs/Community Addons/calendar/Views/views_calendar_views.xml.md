<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/calendar_views.xml

- Module: [[docs/Community Addons/calendar/calendar|calendar]]
- Scope: Community Addons
- Source file: `views/calendar_views.xml`
- Views: 9
- Actions: 7
- Menus: 8
- Rules: 0

## View records

### `res_users_view_form`
- Name: res.users.view.form.inherit.calendar
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_calendar_event_search`
- Name: calendar.event.search
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `categ_ids`, `description`, `location`, `name`, `partner_ids`, `show_as`, `user_id`
- XPath or positional patches: 0

### `view_calendar_event_calendar`
- Name: calendar.event.calendar
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 17
- Sample fields: `accepted_count`, `alarm_ids`, `attendees_count`, `categ_ids`, `declined_count`, `description`, `effective_privacy`, `is_highlighted`, `location`, `partner_id`, and 7 more
- XPath or positional patches: 0

### `view_calendar_event_form_quick_create`
- Name: calendar.event.form.quick_create
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `access_token`, `allday`, `invalid_email_partner_ids`, `location`, `name`, `notes`, `partner_ids`, `privacy`, `recurrence_update`, `start`, and 4 more
- Buttons: `clear_videocall_location`, `set_discuss_videocall_location`
- XPath or positional patches: 0

### `view_calendar_event_form`
- Name: calendar.event.form
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `form`
- Field references: 52
- Sample fields: `accepted_count`, `access_token`, `active`, `alarm_ids`, `allday`, `attendee_ids`, `attendees_count`, `awaiting_count`, `byday`, `categ_ids`, and 42 more
- Buttons: `action_join_video_call`, `action_open_calendar_event`, `action_open_composer`, `action_sendmail`, `clear_videocall_location`, `do_accept`, `do_decline`, `do_tentative`, `set_discuss_videocall_location`
- XPath or positional patches: 0

### `view_calendar_event_tree`
- Name: calendar.event.list
- Model: `calendar.event`
- Type: inferred from arch
- Root tag: `list`
- Field references: 15
- Sample fields: `alarm_ids`, `allday`, `categ_ids`, `description`, `duration`, `location`, `message_needaction`, `name`, `partner_ids`, `privacy`, and 5 more
- Buttons: `action_open_composer`
- XPath or positional patches: 0

### `calendar_alarm_view_form`
- Name: calendar.alarm.form
- Model: `calendar.alarm`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `alarm_type`, `body`, `duration`, `interval`, `mail_template_id`, `name`, `notify_responsible`
- XPath or positional patches: 0

### `view_calendar_alarm_tree`
- Name: calendar.alarm.list
- Model: `calendar.alarm`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `alarm_type`, `duration`, `interval`, `name`
- XPath or positional patches: 0

### `view_calendar_event_type_tree`
- Name: calendar.event.type
- Model: `calendar.event.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `calendar_settings_action`: `act_window` Settings
- `action_view_calendar_event_form`: `view`
- `action_view_calendar_event_tree`: `view`
- `action_view_calendar_event_calendar`: `view`
- `action_calendar_event`: `act_window` Meetings
- `action_calendar_alarm`: `act_window` Calendar Alarm
- `action_calendar_event_type`: `act_window` Meeting Types

## Menus

- `menu_calendar_alarm`: unnamed
- `menu_calendar_event_type`: unnamed
- `menu_calendar_configuration`: Calendar
- `calendar_submenu_reminders`: Reminders
- `menu_calendar_settings`: Settings
- `calendar_menu_config`: Configuration
- `calendar_event_menu`: Calendar
- `mail_menu_calendar`: Calendar

## Navigation

- **Parent:** [[docs/Community Addons/calendar/Views]]

<!-- GENERATED:VIEWFILE -->
