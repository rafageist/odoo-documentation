<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# Profiling

- Module: [[docs/Community Addons/web/web|web]]
- Scope: Community Addons
- Source file: `controllers/profiling.py`
- Base classes: `Controller`
- Routes: 3

## Routes

### `profile`
- Paths: `/web/set_profiling`
- Type: `http`
- Auth: `public`

### `speedscope`
- Paths: `/web/speedscope/<profile>`
- Type: `http`
- Auth: `user`
- Readonly: `True`

### `profile_config`
- Paths: `/web/profile_config/<profile>`
- Type: `http`
- Auth: `user`
- Readonly: `True`

## Navigation

- **Parent:** [[docs/Community Addons/web/Controllers]]

<!-- GENERATED:CONTROLLER -->
