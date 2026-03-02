<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/calendar_views.xml

- Module: [[docs/Community Addons/calendar_sms/calendar_sms|calendar_sms]]
- Scope: Community Addons
- Source file: `views/calendar_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_calendar_event_form_inherited`
- Name: calendar.event.form.calendar_sms
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `calendar.view_calendar_event_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_send_sms`
- XPath or positional patches: 2

### `view_calendar_event_tree_inherited`
- Name: calendar.event.list.calendar_sms
- Model: `calendar.event`
- Type: inferred from arch
- Inherits: `calendar.view_calendar_event_tree`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_send_sms`
- XPath or positional patches: 1

### `calendar_alarm_view_form`
- Name: calendar.alarm.view.form.inherit.calendar.sms
- Model: `calendar.alarm`
- Type: inferred from arch
- Inherits: `calendar.calendar_alarm_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sms_template_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/calendar_sms/Views]]

<!-- GENERATED:VIEWFILE -->
