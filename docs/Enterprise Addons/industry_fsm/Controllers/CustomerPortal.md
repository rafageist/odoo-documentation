<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# CustomerPortal

- Module: [[docs/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]]
- Scope: Enterprise Addons
- Source file: `controllers/portal.py`
- Base classes: `portal.CustomerPortal`
- Routes: 2

## Routes

### `portal_worksheet_outdated`
- Paths: `/my/task/<int:task_id>/worksheet`, `/my/task/<int:task_id>/worksheet/<string:source>`, `/my/task/<int:task_id>/worksheet/sign/<string:source>`
- Type: `http`
- Auth: `public`

### `portal_worksheet_sign`
- Paths: `/my/tasks/<int:task_id>/worksheet/sign/<string:source>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm/Controllers]]

<!-- GENERATED:CONTROLLER -->
