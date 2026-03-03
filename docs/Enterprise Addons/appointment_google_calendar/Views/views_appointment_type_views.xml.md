---
tags: [odoo, enterprise, generated, views]
---

# views/appointment_type_views.xml

- Module: [[docs/Enterprise Addons/appointment_google_calendar/appointment_google_calendar|appointment_google_calendar]]
- Scope: Enterprise Addons
- Source file: `views/appointment_type_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `appointment_type_view_form`
- Name: appointment.type.view.form.inherit.appointment.google.calendar
- Model: `appointment.type`
- Type: inferred from arch
- Inherits: `appointment.appointment_type_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `users_wo_google_calendar_msg`
- Buttons: `%(calendar.calendar_settings_action)d`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment_google_calendar/Views]]

