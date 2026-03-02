<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# WebsiteForumHelpdesk

- Module: [[docs/Enterprise Addons/website_helpdesk_forum/website_helpdesk_forum|website_helpdesk_forum]]
- Scope: Enterprise Addons
- Source file: `controllers/website_forum.py`
- Base classes: `WebsiteForum`
- Routes: 2

## Routes

### `helpdesk_forums`
- Paths: `/helpdesk/<model("helpdesk.team"):team>/forums`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `create_ticket_and_view`
- Paths: `/forum/<model("forum.forum"):forum>/<model("forum.post"):question>/get-forum-data`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_helpdesk_forum/Controllers]]

<!-- GENERATED:CONTROLLER -->
