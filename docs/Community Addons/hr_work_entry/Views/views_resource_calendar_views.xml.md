<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/resource_calendar_views.xml

- Module: [[docs/Community Addons/hr_work_entry/hr_work_entry|hr_work_entry]]
- Scope: Community Addons
- Source file: `views/resource_calendar_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `resource_calendar_leave_view_tree`
- Name: resource.calendar.leaves.list.inherit.hr.work.entry
- Model: `resource.calendar.leaves`
- Type: inferred from arch
- Inherits: `resource.resource_calendar_leave_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `date_to`, `work_entry_type_id`
- XPath or positional patches: 0

### `resource_calendar_leave_view_form`
- Name: resource.calendar.leaves.form.inherit.hr.work.entry
- Model: `resource.calendar.leaves`
- Type: inferred from arch
- Inherits: `resource.resource_calendar_leave_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `resource_id`, `work_entry_type_id`
- XPath or positional patches: 0

### `resource_calendar_attendance_view_form`
- Name: resource.calendar.attendance.form.inherit.hr.work.entry
- Model: `resource.calendar.attendance`
- Type: inferred from arch
- Inherits: `resource.view_resource_calendar_attendance_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `day_period`, `work_entry_type_id`
- XPath or positional patches: 0

### `resource_calendar_attendance_view_tree`
- Name: resource.calendar.attendance.list.inherit.hr.work.entry
- Model: `resource.calendar.attendance`
- Type: inferred from arch
- Inherits: `resource.view_resource_calendar_attendance_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `week_type`, `work_entry_type_id`
- XPath or positional patches: 0

### `resource_calendar_leaves_view_search_inherit`
- Name: resource.calendar.leaves.search.inherit
- Model: `resource.calendar.leaves`
- Type: inferred from arch
- Inherits: `resource.view_resource_calendar_leaves_search`
- Root tag: `filter`
- Field references: 1
- Sample fields: `work_entry_type_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/hr_work_entry/Views]]

<!-- GENERATED:VIEWFILE -->
