<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# ShiftController

- Module: [[docs/Enterprise Addons/planning/planning|planning]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 10

## Routes

### `planning`
- Paths: `/planning/<string:planning_token>/<string:employee_token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `planning_self_assign`
- Paths: `/planning/<string:token_planning>/<string:token_employee>/assign/<int:slot_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `planning_self_unassign`
- Paths: `/planning/<string:token_planning>/<string:token_employee>/unassign/<int:shift_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `planning_switch_shift`
- Paths: `/planning/<string:token_planning>/<string:token_employee>/switch/<int:shift_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `planning_cancel_shift_switch`
- Paths: `/planning/<string:token_planning>/<string:token_employee>/cancel_switch/<int:shift_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `planning_self_assign_with_user_from_calendar`
- Paths: `/planning/<string:token_planning>/<string:token_employee>/take_open_shift/<int:shift_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `planning_self_assign_with_user`
- Paths: `/planning/assign/<string:token_employee>/<int:shift_id>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `planning_self_unassign_with_user`
- Paths: `/planning/unassign/<string:token_employee>/<int:shift_id>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `slot_get_ics_file`
- Paths: `/slot/<string:access_token>.ics`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `planning_get_ics_file`
- Paths: `/planning/<string:planning_token>/<string:employee_token>.ics`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Enterprise Addons/planning/Controllers]]

<!-- GENERATED:CONTROLLER -->
