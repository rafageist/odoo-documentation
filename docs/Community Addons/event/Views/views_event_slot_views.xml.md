<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_slot_views.xml

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Source file: `views/event_slot_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_event_slot_calendar`
- Name: event.slot.calendar
- Model: `event.slot`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 3
- Sample fields: `date_tz`, `end_datetime`, `start_datetime`
- XPath or positional patches: 0

### `view_event_slot_tree`
- Name: event.slot.list
- Model: `event.slot`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `color`, `date`, `end_hour`, `start_hour`
- Buttons: `durationArrow`
- XPath or positional patches: 0

### `view_event_slot_multi_create_form`
- Name: event.slot.form
- Model: `event.slot`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `color`, `date_tz`, `event_id`
- XPath or positional patches: 0

### `view_event_slot_form`
- Name: event.slot.form
- Model: `event.slot`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `color`, `date_tz`, `end_hour`, `event_id`, `start_hour`
- XPath or positional patches: 0

## Actions

- `event_slot_action_from_event`: `act_window` Slots

## Navigation

- **Parent:** [[docs/Community Addons/event/Views]]

<!-- GENERATED:VIEWFILE -->
