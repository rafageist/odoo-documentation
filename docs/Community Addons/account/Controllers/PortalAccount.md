<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# PortalAccount

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `controllers/portal.py`
- Base classes: `CustomerPortal`
- Routes: 3

## Routes

### `portal_my_invoices`
- Paths: `/my/invoices`, `/my/invoices/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_invoice_detail`
- Paths: `/my/invoices/<int:invoice_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `portal_my_journal_unsubscribe`
- Paths: `/my/journal/<int:journal_id>/unsubscribe`
- Type: `http`
- Auth: `user`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/account/Controllers]]

<!-- GENERATED:CONTROLLER -->
