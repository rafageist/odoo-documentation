<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/appointment_type_views.xml

- Module: [[docs/Enterprise Addons/website_appointment/website_appointment|website_appointment]]
- Scope: Enterprise Addons
- Source file: `views/appointment_type_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `appointment_type_view_search`
- Name: appointment.type.search.inherit.website
- Model: `appointment.type`
- Type: inferred from arch
- Inherits: `appointment.appointment_type_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `appointment_type_view_form_add_simplified`
- Name: appointment.type.view.form.add.simplified
- Model: `appointment.type`
- Type: inferred from arch
- Inherits: `appointment.appointment_type_view_form_add_simplified`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `website_url`
- XPath or positional patches: 6

### `appointment_type_view_form`
- Name: appointment.type.view.form.inherit.website
- Model: `appointment.type`
- Type: inferred from arch
- Inherits: `appointment.appointment_type_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `is_published`, `website_id`, `website_url`
- XPath or positional patches: 2

### `appointment_type_view_tree`
- Name: appointment.type.list.inherit.website.appointment
- Model: `appointment.type`
- Type: inferred from arch
- Inherits: `appointment.appointment_type_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `is_published`
- XPath or positional patches: 1

### `appointment_type_view_kanban`
- Name: appointment.type.view.kanban.inherit.website
- Model: `appointment.type`
- Type: inferred from arch
- Inherits: `appointment.appointment_type_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `is_published`
- XPath or positional patches: 2

## Actions

- `appointment_type_action_add_simplified`: `act_window` New Appointment Type

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_appointment/Views]]

<!-- GENERATED:VIEWFILE -->
