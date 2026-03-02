<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/project_milestone_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `views/project_milestone_views.xml`
- Views: 3
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `project_milestone_view_kanban`
- Name: project.milestone.view.kanban
- Model: `project.milestone`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `can_be_marked_as_done`, `deadline`, `is_deadline_exceeded`, `is_reached`, `name`
- XPath or positional patches: 0

### `project_milestone_view_tree`
- Name: project.milestone.view.list
- Model: `project.milestone`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `deadline`, `is_reached`, `name`, `sequence`
- Buttons: `action_view_tasks`
- XPath or positional patches: 0

### `project_milestone_view_form`
- Name: project.milestone.view.form
- Model: `project.milestone`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `deadline`, `done_task_count`, `is_reached`, `name`, `project_id`, `task_count`
- Buttons: `%(project.action_view_task_from_milestone)d`
- XPath or positional patches: 0

## Actions

- `action_view_project_milestone_form`: `view`
- `action_view_project_milestone_kanban`: `view`
- `action_view_project_milestone_list`: `view`
- `project_milestone_action`: `act_window` Milestones

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

<!-- GENERATED:VIEWFILE -->
