<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/project_role_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `views/project_role_views.xml`
- Views: 4
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `project_role_view_search`
- Name: project.role.search
- Model: `project.role`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `project_role_view_kanban`
- Name: project.role.kanban
- Model: `project.role`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `color`, `name`
- XPath or positional patches: 0

### `project_role_view_form`
- Name: project.role.form
- Model: `project.role`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `active`, `color`, `name`
- XPath or positional patches: 0

### `project_role_view_list`
- Name: project.role.list
- Model: `project.role`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `color`, `name`, `sequence`
- XPath or positional patches: 0

## Actions

- `project_roles_action_kanban`: `view`
- `project_roles_action_list`: `view`
- `project_roles_action`: `act_window` Project Roles

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

<!-- GENERATED:VIEWFILE -->
