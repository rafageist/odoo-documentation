<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_event_views.xml

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Source file: `views/event_event_views.xml`
- Views: 7
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `view_event_search`
- Name: event.event.search
- Model: `event.event`
- Type: inferred from arch
- Root tag: `search`
- Field references: 8
- Sample fields: `activity_type_id`, `activity_user_id`, `address_search`, `event_type_id`, `name`, `question_ids`, `stage_id`, `user_id`
- XPath or positional patches: 0

### `view_event_calendar`
- Name: event.event.calendar
- Model: `event.event`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 5
- Sample fields: `event_type_id`, `seats_reserved`, `seats_taken`, `seats_used`, `user_id`
- XPath or positional patches: 0

### `view_event_kanban`
- Name: event.event.kanban
- Model: `event.event`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `activity_ids`, `address_id`, `date_begin`, `date_end`, `kanban_state`, `name`, `seats_taken`, `stage_id`, `user_id`
- XPath or positional patches: 0

### `event_event_view_form_quick_create`
- Name: event.event.form.quick_create
- Model: `event.event`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `date_begin`, `date_end`, `name`
- XPath or positional patches: 0

### `event_event_view_activity`
- Name: event.event.view.activity
- Model: `event.event`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 3
- Sample fields: `date_begin`, `name`, `user_id`
- XPath or positional patches: 0

### `view_event_tree`
- Name: event.event.list
- Model: `event.event`
- Type: inferred from arch
- Root tag: `list`
- Field references: 15
- Sample fields: `activity_exception_decoration`, `address_id`, `company_id`, `date_begin`, `date_end`, `message_needaction`, `name`, `organizer_id`, `seats_max`, `seats_reserved`, and 5 more
- XPath or positional patches: 0

### `view_event_form`
- Name: event.event.form
- Model: `event.event`
- Type: inferred from arch
- Root tag: `form`
- Field references: 42
- Sample fields: `active`, `address_id`, `answer_ids`, `badge_format`, `badge_image`, `company_id`, `date_begin`, `date_end`, `date_tz`, `event_mail_ids`, and 32 more
- Buttons: `%(event.act_event_registration_from_event)d`, `%(event.event_registration_action_stats_from_event)d`, `%(event_barcode_action_main_view)d`, `action_open_slot_calendar`, `action_view_question_answers`
- XPath or positional patches: 0

## Actions

- `action_event_view`: `act_window` Events
- `event_barcode_action_main_view`: `client` Barcode Interface

## Menus

- `menu_event_registration_desk`: Registration Desk
- `event.menu_event_event`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/event/Views]]

<!-- GENERATED:VIEWFILE -->
