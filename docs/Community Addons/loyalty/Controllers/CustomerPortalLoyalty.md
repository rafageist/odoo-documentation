<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# CustomerPortalLoyalty

- Module: [[docs/Community Addons/loyalty/loyalty|loyalty]]
- Scope: Community Addons
- Source file: `controllers/portal.py`
- Base classes: `CustomerPortal`
- Routes: 2

## Routes

### `portal_my_loyalty_card_history`
- Paths: `/my/loyalty_card/<int:card_id>/history`, `/my/loyalty_card/<int:card_id>/history/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_get_card_history_values`
- Paths: `/my/loyalty_card/<int:card_id>/values`
- Type: `jsonrpc`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Community Addons/loyalty/Controllers]]

<!-- GENERATED:CONTROLLER -->
