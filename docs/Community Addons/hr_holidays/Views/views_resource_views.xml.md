<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/resource_views.xml

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Source file: `views/resource_views.xml`
- Views: 5
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `resource_calendar_view_tree`
- Name: resource.calendar.view.list.inherit.hr.holidays
- Model: `resource.calendar`
- Type: inferred from arch
- Inherits: `resource.view_resource_calendar_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `associated_leaves_count`, `work_resources_count`
- XPath or positional patches: 0

### `resource_calendar_form_inherit`
- Name: resource.calendar.form.inherit
- Model: `resource.calendar`
- Type: inferred from arch
- Inherits: `resource.resource_calendar_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `associated_leaves_count`
- Buttons: `%(resource_calendar_global_leaves_action_from_calendar)d`
- XPath or positional patches: 1

### `resource_calendar_leaves_tree_inherit`
- Name: resource.calendar.leaves.list.inherit
- Model: `resource.calendar.leaves`
- Type: inferred from arch
- Inherits: `resource.resource_calendar_leave_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `company_id`
- XPath or positional patches: 6

### `resource_calendar_leave_form_inherit`
- Name: resource.calendar.leaves.form.inherit
- Model: `resource.calendar.leaves`
- Type: inferred from arch
- Inherits: `resource.resource_calendar_leave_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `holiday_id`, `name`
- XPath or positional patches: 0

### `resource_calendar_leaves_view_search_inherit`
- Name: resource.calendar.leaves.search.inherit
- Model: `resource.calendar.leaves`
- Type: inferred from arch
- Inherits: `resource.view_resource_calendar_leaves_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `open_view_public_holiday`: `act_window` Public Holidays
- `resource_calendar_global_leaves_action_from_calendar`: `act_window` Public Holidays

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Views]]

<!-- GENERATED:VIEWFILE -->
