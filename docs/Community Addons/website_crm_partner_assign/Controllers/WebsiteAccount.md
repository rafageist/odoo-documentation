<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteAccount

- Module: [[docs/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `CustomerPortal`
- Routes: 4

## Routes

### `portal_my_leads`
- Paths: `/my/leads`, `/my/leads/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_opportunities`
- Paths: `/my/opportunities`, `/my/opportunities/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_lead`
- Paths: `/my/lead/<model('crm.lead', "[('type','=', 'lead')]"):lead>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_opportunity`
- Paths: `/my/opportunity/<model('crm.lead', "[('type','=', 'opportunity')]"):opp>`
- Type: `http`
- Auth: `user`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website_crm_partner_assign/Controllers]]

<!-- GENERATED:CONTROLLER -->
