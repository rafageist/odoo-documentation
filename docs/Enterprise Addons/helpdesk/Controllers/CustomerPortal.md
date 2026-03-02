<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# CustomerPortal

- Module: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]]
- Scope: Enterprise Addons
- Source file: `controllers/portal.py`
- Base classes: `portal.CustomerPortal`
- Routes: 3

## Routes

### `my_helpdesk_tickets`
- Paths: `/my/tickets`, `/my/tickets/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `tickets_followup`
- Paths: `/helpdesk/ticket/<int:ticket_id>`, `/helpdesk/ticket/<int:ticket_id>/<access_token>`, `/my/ticket/<int:ticket_id>`, `/my/ticket/<int:ticket_id>/<access_token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `ticket_close`
- Paths: `/my/ticket/close/<int:ticket_id>`, `/my/ticket/close/<int:ticket_id>/<access_token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk/Controllers]]

<!-- GENERATED:CONTROLLER -->
