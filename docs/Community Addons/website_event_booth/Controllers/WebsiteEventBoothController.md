<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteEventBoothController

- Module: [[docs/Community Addons/website_event_booth/website_event_booth|website_event_booth]]
- Scope: Community Addons
- Source file: `controllers/event_booth.py`
- Base classes: `WebsiteEventController`
- Routes: 6

## Routes

### `event_booth_main`
- Paths: `/event/<model("event.event"):event>/booth`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `event_booth_register`
- Paths: `/event/<model("event.event"):event>/booth/register`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `event_booth_contact_form`
- Paths: `/event/<model("event.event"):event>/booth/register_form`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `event_booth_registration_confirm`
- Paths: `/event/<model("event.event"):event>/booth/confirm`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `check_booths_availability`
- Paths: `/event/booth/check_availability`
- Type: `jsonrpc`
- Auth: `public`

### `get_booth_category_available_booths`
- Paths: `/event/booth_category/get_available_booths`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/website_event_booth/Controllers]]

<!-- GENERATED:CONTROLLER -->
