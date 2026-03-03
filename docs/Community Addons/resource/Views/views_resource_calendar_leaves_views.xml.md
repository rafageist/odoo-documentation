---
tags: [odoo, community, generated, views]
---

# views/resource_calendar_leaves_views.xml

- Module: [[docs/Community Addons/resource/resource|resource]]
- Scope: Community Addons
- Source file: `views/resource_calendar_leaves_views.xml`
- Views: 4
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `resource_calendar_leave_tree`
- Name: resource.calendar.leaves.list
- Model: `resource.calendar.leaves`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `calendar_id`, `company_id`, `date_from`, `date_to`, `name`, `resource_id`
- XPath or positional patches: 0

### `resource_calendar_leave_form`
- Name: resource.calendar.leaves.form
- Model: `resource.calendar.leaves`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `calendar_id`, `company_id`, `date_from`, `date_to`, `name`, `resource_id`
- XPath or positional patches: 0

### `view_resource_calendar`
- Name: resource.calendar.leaves.calendar
- Model: `resource.calendar.leaves`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 3
- Sample fields: `company_id`, `name`, `resource_id`
- XPath or positional patches: 0

### `view_resource_calendar_leaves_search`
- Name: resource.calendar.leaves.search
- Model: `resource.calendar.leaves`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `calendar_id`, `company_id`, `name`, `resource_id`
- XPath or positional patches: 0

## Actions

- `resource_calendar_resources_leaves`: `act_window` Resources Time Off
- `resource_calendar_closing_days`: `act_window` Closing Days
- `resource_calendar_leaves_action_from_calendar`: `act_window` Resource Time Off
- `action_resource_calendar_leave_tree`: `act_window` Resource Time Off

## Navigation

- **Parent:** [[docs/Community Addons/resource/Views]]

