---
tags: [odoo, community, generated, views]
---

# views/project_sharing_views.xml

- Module: [[docs/Community Addons/sale_project/sale_project|sale_project]]
- Scope: Community Addons
- Source file: `views/project_sharing_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `project_sharing_inherit_project_task_view_tree`
- Name: project.task.view.list.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `allow_billable`, `allow_milestones`
- XPath or positional patches: 1

### `project_sharing_inherit_project_task_view_form`
- Name: project.task.view.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_form`
- Root tag: `div`
- Field references: 3
- Sample fields: `allow_billable`, `display_sale_order_button`, `sale_line_id`
- Buttons: `action_project_sharing_view_so`
- XPath or positional patches: 7

## Actions

- `project.project_sharing_project_task_action`: `act_window`

## Navigation

- **Parent:** [[docs/Community Addons/sale_project/Views]]

