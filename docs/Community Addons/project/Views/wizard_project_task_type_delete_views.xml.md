<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizard/project_task_type_delete_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `wizard/project_task_type_delete_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_project_task_type_unarchive_wizard`
- Name: project.task.type.delete.wizard.form
- Model: `project.task.type.delete.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 0
- Buttons: `action_unarchive_task`
- XPath or positional patches: 0

### `view_project_task_type_delete_confirmation_wizard`
- Name: project.task.type.delete.wizard.form
- Model: `project.task.type.delete.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `name`, `project_ids`
- Buttons: `action_confirm`
- XPath or positional patches: 0

### `view_project_task_type_delete_wizard`
- Name: project.task.type.delete.wizard.form
- Model: `project.task.type.delete.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `stages_active`, `tasks_count`
- Buttons: `action_archive`, `action_unlink`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

<!-- GENERATED:VIEWFILE -->
