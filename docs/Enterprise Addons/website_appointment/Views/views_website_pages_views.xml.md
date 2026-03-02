<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/website_pages_views.xml

- Module: [[docs/Enterprise Addons/website_appointment/website_appointment|website_appointment]]
- Scope: Enterprise Addons
- Source file: `views/website_pages_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `appointment_pages_kanban_view`
- Name: Appointments Pages Kanban
- Model: `appointment.type`
- Type: inferred from arch
- Inherits: `appointment_type_view_kanban`
- Root tag: `kanban`
- Field references: 0
- XPath or positional patches: 1

### `appointment_pages_tree_view`
- Name: Appointments Pages List
- Model: `appointment.type`
- Type: inferred from arch
- Inherits: `appointment.appointment_type_view_tree`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `is_published`, `is_seo_optimized`, `name`, `website_id`, `website_url`
- XPath or positional patches: 2

## Actions

- `action_appointment_pages_list`: `act_window` Appointment Pages

## Menus

- `menu_appointment_pages`: Appointments

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_appointment/Views]]

<!-- GENERATED:VIEWFILE -->
