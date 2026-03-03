---
tags: [odoo, enterprise, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Enterprise Addons/project_enterprise/project_enterprise|project_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/project_task_views.xml`
- Views: 17
- Actions: 18
- Menus: 0
- Rules: 0

## View records

### `project_task_view_gantt_res_partner`
- Name: project.task.view.gantt.res.partner
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_gantt_inherit_all_task`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_form_in_gantt_res_partner`
- Name: project.task.view.form.gantt.res.partner
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_form_in_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_task_calendar_inherited`
- Name: project.task.all.calendar
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_calendar`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_map_view_no_title_no_milestone`
- Name: project.task.view.map.no.milestone
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_map_view_no_title`
- Root tag: `field`
- Field references: 1
- Sample fields: `milestone_id`
- XPath or positional patches: 0

### `project_task_map_view_no_title`
- Name: project.task.view.map
- Model: `project.task`
- Type: inferred from arch
- Root tag: `map`
- Field references: 3
- Sample fields: `milestone_id`, `partner_id`, `user_names`
- XPath or positional patches: 0

### `project_task_map_view`
- Name: project.task.view.map
- Model: `project.task`
- Type: inferred from arch
- Root tag: `map`
- Field references: 5
- Sample fields: `milestone_id`, `partner_id`, `planned_date_begin`, `project_id`, `user_names`
- XPath or positional patches: 0

### `project_task_dependency_view_gantt`
- Name: project.task.dependency.view.gantt
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.project_task_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_gantt_view_project_milestone`
- Name: project.task.my.gantt.inherit.project.milestone
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_gantt_inherit_my_task`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_task_gantt_inherit_my_task`
- Name: project.task.my.gantt
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_gantt`
- Root tag: `gantt`
- Field references: 0
- XPath or positional patches: 1

### `view_task_gantt_inherit_all_task`
- Name: project.task.all.gantt
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_gantt`
- Name: project.task.view.gantt
- Model: `project.task`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 0
- Buttons: `action_unschedule_task`
- XPath or positional patches: 0

### `view_task_kanban_inherited_project_enterprise`
- Name: project.task.kanban.project.enterprise
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_form_in_gantt`
- Name: project.task.view.form.gantt
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_unschedule_task`
- XPath or positional patches: 1

### `project_task_view_form`
- Name: project.task.view.form.inherit.project.enterprise
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_form2`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `dependency_warning`, `planned_date_begin`, `planning_overlap`
- XPath or positional patches: 9

### `view_ebterprise_task_tree2`
- Name: project.task.list
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_tree2`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_tree`
- Name: project.task.view.list.inherit.project.enterprise
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_task_view_tree_base`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `planned_date_begin`
- XPath or positional patches: 2

### `project_task_view_search_conflict_task_project_enterprise`
- Name: project.task.view.search.conflict.task.project.enterprise
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_search_form_project_fsm_base`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `project_milestone_action_view_tasks_gantt`: `view`
- `project_task_action_from_partner_gantt_view`: `view`
- `project.project_task_action_from_partner`: `act_window`
- `project.project_task_action_sub_task`: `act_window`
- `project_task_from_milestone_action_map_view`: `view`
- `action_view_task_from_milestone_calendar_view`: `view`
- `action_view_task_from_milestone_gantt_view`: `view`
- `action_view_task_from_milestone_tree_view`: `view`
- `action_view_task_from_milestone_kanban_view`: `view`
- `project.action_view_task_from_milestone`: `act_window`
- `project_task_map_action_view`: `view`
- `project_all_task_map_action_view`: `view`
- `project_all_task_gantt_action_view`: `view`
- `open_view_all_task_list_gantt`: `view`
- `project.action_view_all_task`: `act_window`
- `open_view_my_task_list_gantt`: `view`
- `project.action_view_my_task`: `act_window`
- `project.action_view_task`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_enterprise/Views]]

