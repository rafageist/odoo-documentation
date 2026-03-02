<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteEventController

- Module: [[docs/Community Addons/website_event/website_event|website_event]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 8

## Routes

### `events`
- Paths: `<dynamic>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `event_page`
- Paths: `/event/<model("event.event"):event>/page/<path:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `event`
- Paths: `/event/<model("event.event"):event>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `event_register`
- Paths: `/event/<model("event.event"):event>/register`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `registration_tickets`
- Paths: `/event/<model("event.event"):event>/registration/slot/<int:slot_id>/tickets`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `registration_new`
- Paths: `/event/<model("event.event"):event>/registration/new`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `registration_confirm`
- Paths: `/event/<model("event.event"):event>/registration/confirm`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `event_registration_success`
- Paths: `/event/<model("event.event"):event>/registration/success`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website_event/Controllers]]

<!-- GENERATED:CONTROLLER -->
