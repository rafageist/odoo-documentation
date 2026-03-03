---
tags: [odoo, enterprise, generated, views]
---

# views/resource_views.xml

- Module: [[docs/Enterprise Addons/planning/planning|planning]]
- Scope: Enterprise Addons
- Source file: `views/resource_views.xml`
- Views: 7
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `resource_resource_kanban_view`
- Name: unnamed
- Model: `resource.resource`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `color`, `name`, `role_ids`
- XPath or positional patches: 0

### `resource_resource_search_view_inherit`
- Name: unnamed
- Model: `resource.resource`
- Type: inferred from arch
- Inherits: `resource.view_resource_resource_search`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `calendar_id`, `default_role_id`, `role_ids`
- XPath or positional patches: 9

### `resource_resource_search_view_roles`
- Name: resource.resource.search.view.roles
- Model: `resource.resource`
- Type: inferred from arch
- Inherits: `resource.view_resource_resource_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `role_ids`
- XPath or positional patches: 1

### `resource_resource_tree_view_inherit`
- Name: unnamed
- Model: `resource.resource`
- Type: inferred from arch
- Inherits: `resource.resource_resource_tree`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `color`, `default_role_id`, `role_ids`
- XPath or positional patches: 9

### `resource_resource_form_view_inherit`
- Name: unnamed
- Model: `resource.resource`
- Type: inferred from arch
- Inherits: `resource_resource_with_employee_form_view_inherit`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `color`, `default_role_id`, `role_ids`
- XPath or positional patches: 4

### `resource_resource_with_employee_form_view_inherit`
- Name: unnamed
- Model: `resource.resource`
- Type: inferred from arch
- Inherits: `resource.resource_resource_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `resource_resource_form_tags_view_inherit`
- Name: unnamed
- Model: `resource.resource`
- Type: inferred from arch
- Inherits: `resource.resource_resource_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

## Actions

- `planning_action_resources`: `act_window` Materials

## Navigation

- **Parent:** [[docs/Enterprise Addons/planning/Views]]

