<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# ReportController

- Module: [[docs/Community Addons/web/web|web]]
- Scope: Community Addons
- Source file: `controllers/report.py`
- Base classes: `http.Controller`
- Routes: 4

## Routes

### `report_routes`
- Paths: `/report/<converter>/<reportname>`, `/report/<converter>/<reportname>/<docids>`
- Type: `http`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `report_barcode`
- Paths: `/report/barcode`, `/report/barcode/<barcode_type>/<path:value>`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `report_download`
- Paths: `/report/download`
- Type: `http`
- Auth: `user`

### `check_wkhtmltopdf`
- Paths: `/report/check_wkhtmltopdf`
- Type: `jsonrpc`
- Auth: `user`
- Readonly: `True`

## Navigation

- **Parent:** [[docs/Community Addons/web/Controllers]]

<!-- GENERATED:CONTROLLER -->
