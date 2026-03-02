<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# CustomerPortal

- Module: [[docs/Community Addons/mrp_subcontracting/mrp_subcontracting|mrp_subcontracting]]
- Scope: Community Addons
- Source file: `controllers/portal.py`
- Base classes: `portal.CustomerPortal`
- Routes: 3

## Routes

### `portal_my_productions`
- Paths: `/my/productions`, `/my/productions/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_production`
- Paths: `/my/productions/<int:picking_id>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `render_production_backend_view`
- Paths: `/my/productions/<int:picking_id>/subcontracting_portal`
- Type: `http`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Community Addons/mrp_subcontracting/Controllers]]

<!-- GENERATED:CONTROLLER -->
