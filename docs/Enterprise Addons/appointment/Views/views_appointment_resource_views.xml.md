<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/appointment_resource_views.xml

- Module: [[docs/Enterprise Addons/appointment/appointment|appointment]]
- Scope: Enterprise Addons
- Source file: `views/appointment_resource_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `appointment_resource_view_tree`
- Name: appointment.resource.view.list
- Model: `appointment.resource`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `appointment_type_ids`, `capacity`, `company_id`, `linked_resource_ids`, `name`, `resource_calendar_id`, `sequence`, `shareable`
- XPath or positional patches: 0

### `appointment_resource_view_form`
- Name: appointment.resource.view.form
- Model: `appointment.resource`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `active`, `capacity`, `company_id`, `description`, `image_1920`, `linked_resource_ids`, `name`, `resource_calendar_id`, `resource_id`, `shareable`, and 1 more
- XPath or positional patches: 0

### `appointment_resource_view_search`
- Name: appointment.resource.view.search
- Model: `appointment.resource`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `appointment_type_ids`, `capacity`, `name`
- XPath or positional patches: 0

## Actions

- `appointment_resource_action_stat`: `act_window` Resources
- `appointment_resource_action`: `act_window` Resources

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment/Views]]

<!-- GENERATED:VIEWFILE -->
