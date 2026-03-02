<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# ExhibitorController

- Module: [[docs/Community Addons/website_event_exhibitor/website_event_exhibitor|website_event_exhibitor]]
- Scope: Community Addons
- Source file: `controllers/exhibitor.py`
- Base classes: `WebsiteEventController`
- Routes: 3

## Routes

### `event_exhibitors`
- Paths: `/event/<model("event.event"):event>/exhibitor`, `/event/<model("event.event"):event>/exhibitors`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `event_exhibitor`
- Paths: `/event/<model("event.event", "[('exhibitor_menu', '=', True)]"):event>/exhibitor/<model("event.sponsor", "[('event_id', '=', event.id)]"):sponsor>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `event_sponsor_read`
- Paths: `/event_sponsor/<int:sponsor_id>/read`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website_event_exhibitor/Controllers]]

<!-- GENERATED:CONTROLLER -->
