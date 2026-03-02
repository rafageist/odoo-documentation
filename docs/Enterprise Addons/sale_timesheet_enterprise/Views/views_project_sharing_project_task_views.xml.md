<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/project_sharing_project_task_views.xml

- Module: [[docs/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/project_sharing_project_task_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `project_sharing_inherit_project_task_view_tree`
- Name: sale_timesheet_enterprise.project.task.view.list.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 5

### `project_sharing_kanban_inherit_project_task_view_kanban`
- Name: sale_timesheet_enterprise.project.sharing.project.task.kanban.inherited
- Model: `project.task`
- Type: inferred from arch
- Inherits: `hr_timesheet.project_sharing_kanban_inherit_project_task_view_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 5

### `project_sharing_inherit_project_task_view_form`
- Name: project.sharing.inherit.project.task.view.form
- Model: `project.task`
- Type: inferred from arch
- Inherits: `sale_timesheet.project_sharing_inherit_project_task_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 17

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_timesheet_enterprise/Views]]

<!-- GENERATED:VIEWFILE -->
