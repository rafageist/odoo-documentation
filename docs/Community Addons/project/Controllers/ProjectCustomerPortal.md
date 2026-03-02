<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# ProjectCustomerPortal

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `controllers/portal.py`
- Base classes: `CustomerPortal`
- Routes: 9

## Routes

### `portal_my_projects`
- Paths: `/my/projects`, `/my/projects/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_project`
- Paths: `/my/projects/<int:project_id>`, `/my/projects/<int:project_id>/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `render_project_backend_view`
- Paths: `/my/projects/<int:project_id>/project_sharing`, `/my/projects/<int:project_id>/project_sharing/<path:subpath>`
- Type: `http`
- Auth: `user`

### `portal_my_project_task`
- Paths: `/my/projects/<int:project_id>/task/<int:task_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `portal_my_project_subtasks`
- Paths: `/my/projects/<int:project_id>/task/<int:task_id>/subtasks`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_project_recurrent_tasks`
- Paths: `/my/projects/<int:project_id>/task/<int:task_id>/recurrent_tasks`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_tasks`
- Paths: `/my/tasks`, `/my/tasks/page/<int:page>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `portal_my_task`
- Paths: `/my/tasks/<int:task_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `add_image`
- Paths: `/project_sharing/attachment/add_image`
- Type: `http`
- Auth: `user`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/project/Controllers]]

<!-- GENERATED:CONTROLLER -->
