<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# AppointmentController

- Module: [[docs/Enterprise Addons/appointment/appointment|appointment]]
- Scope: Enterprise Addons
- Source file: `controllers/appointment.py`
- Base classes: `http.Controller`
- Routes: 12

## Routes

### `appointment_invite`
- Paths: `/book/<string:short_code>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `appointment_type_index_old`
- Paths: `/calendar`, `/calendar/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `appointment_type_index`
- Paths: `/appointment`, `/appointment/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `appointment_type_page_old`
- Paths: `/calendar/<string:appointment_type>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `appointment_type_page`
- Paths: `/appointment/<int:appointment_type_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `appointment_staff_user_avatar`
- Paths: `/appointment/<int:appointment_type_id>/avatar`
- Type: `http`
- Auth: `public`

### `appointment_resource_avatar`
- Paths: `/appointment/<int:appointment_type_id>/resource_avatar`
- Type: `http`
- Auth: `public`

### `appointment_type_id_form`
- Paths: `/appointment/<int:appointment_type_id>/info`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `appointment_form_submit`
- Paths: `/appointment/<int:appointment_type_id>/submit`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `get_upcoming_appointments`
- Paths: `/appointment/get_upcoming_appointments`
- Type: `jsonrpc`
- Auth: `public`

### `get_appointment_message_intro`
- Paths: `/appointment/<int:appointment_type_id>/get_message_intro`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `appointment_update_available_slots`
- Paths: `/appointment/<int:appointment_type_id>/update_available_slots`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment/Controllers]]

<!-- GENERATED:CONTROLLER -->
