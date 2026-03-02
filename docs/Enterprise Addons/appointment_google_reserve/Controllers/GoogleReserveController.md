<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# GoogleReserveController

- Module: [[docs/Enterprise Addons/appointment_google_reserve/appointment_google_reserve|appointment_google_reserve]]
- Scope: Enterprise Addons
- Source file: `controllers/google_reserve.py`
- Base classes: `Controller`
- Routes: 4

## Routes

### `google_reserve_batch_availability_lookup`
- Paths: `/appointment/<int:appointment_id>/<string:appointment_token>/google_reserve/availabilities`
- Auth: `public`

### `google_reserve_booking_create`
- Paths: `/appointment/<int:appointment_id>/<string:appointment_token>/google_reserve/booking/create`
- Auth: `public`

### `google_reserve_booking_update`
- Paths: `/appointment/<int:appointment_id>/<string:appointment_token>/google_reserve/booking/<int:calendar_event_id>/update`
- Auth: `public`

### `google_reserve_upload_availabilities_feed`
- Paths: `/appointment/google_reserve/upload_availabilities_feed`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment_google_reserve/Controllers]]

<!-- GENERATED:CONTROLLER -->
