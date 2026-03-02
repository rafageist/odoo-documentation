<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# WebsiteHelpdesk

- Module: [[docs/Enterprise Addons/website_helpdesk/website_helpdesk|website_helpdesk]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 3

## Routes

### `website_helpdesk_teams`
- Paths: `/helpdesk`, `/helpdesk/<model("helpdesk.team"):team>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `website_helpdesk_knowledge_base`
- Paths: `/helpdesk/<model("helpdesk.team"):team>/knowledgebase`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `website_helpdesk_autocomplete`
- Paths: `/helpdesk/<model("helpdesk.team"):team>/knowledgebase/autocomplete`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_helpdesk/Controllers]]

<!-- GENERATED:CONTROLLER -->
