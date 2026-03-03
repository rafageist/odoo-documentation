---
tags: [odoo, community, generated, views]
---

# views/resource_calendar_views.xml

- Module: [[docs/Community Addons/resource/resource|resource]]
- Scope: Community Addons
- Source file: `views/resource_calendar_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_resource_calendar_tree`
- Name: resource.calendar.list
- Model: `resource.calendar`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_id`, `full_time_required_hours`, `hours_per_week`, `name`, `schedule_type`, `work_resources_count`, `work_time_rate`
- XPath or positional patches: 0

### `resource_calendar_form`
- Name: resource.calendar.form
- Model: `resource.calendar`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `attendance_ids`, `attendance_ids_1st_week`, `attendance_ids_2nd_week`, `company_id`, `full_time_required_hours`, `hours_per_day`, `hours_per_week`, `name`, `schedule_type`, `two_weeks_explanation`, and 4 more
- Buttons: `%(resource_calendar_leaves_action_from_calendar)d`, `%(resource_resource_action_from_calendar)d`, `switch_based_on_duration`, `switch_calendar_type`
- XPath or positional patches: 0

### `view_resource_calendar_search`
- Name: resource.calendar.search
- Model: `resource.calendar`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `company_id`, `name`
- XPath or positional patches: 0

## Actions

- `action_resource_calendar_form`: `act_window` Working Schedules

## Navigation

- **Parent:** [[docs/Community Addons/resource/Views]]

