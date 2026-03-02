<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# DashboardShareRoute

- Module: [[docs/Community Addons/spreadsheet_dashboard/spreadsheet_dashboard|spreadsheet_dashboard]]
- Scope: Community Addons
- Source file: `controllers/share.py`
- Base classes: `http.Controller`
- Routes: 3

## Routes

### `share_portal`
- Paths: `/dashboard/share/<int:share_id>/<token>`
- Type: `http`
- Auth: `public`

### `download`
- Paths: `/dashboard/download/<int:share_id>/<token>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `get_shared_dashboard_data`
- Paths: `/dashboard/data/<int:share_id>/<token>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

## Navigation

- **Parent:** [[docs/Community Addons/spreadsheet_dashboard/Controllers]]

<!-- GENERATED:CONTROLLER -->
