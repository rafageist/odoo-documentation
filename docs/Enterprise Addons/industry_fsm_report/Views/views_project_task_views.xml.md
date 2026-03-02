<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm_report/industry_fsm_report|industry_fsm_report]]
- Scope: Enterprise Addons
- Source file: `views/project_task_views.xml`
- Views: 14
- Actions: 22
- Menus: 0
- Rules: 0

## View records

### `project_task_view_mobile_form_inherit`
- Name: industry_fsm_sale.project.task.view.mobile.form
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_view_mobile_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_list_fsm_inherit`
- Name: project.task.list.fsm.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_view_list_fsm`
- Root tag: `field`
- Field references: 1
- Sample fields: `worksheet_template_id`
- XPath or positional patches: 0

### `view_task_tree2_inherited`
- Name: project.task.list.inherited
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_task_view_tree_base`
- Root tag: `field`
- Field references: 2
- Sample fields: `project_id`, `worksheet_template_id`
- XPath or positional patches: 0

### `project_task_graph_view_groupby_worksheet`
- Name: project.task.graph.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `worksheet_template_id`
- XPath or positional patches: 1

### `project_task_pivot_view_groupby_worksheet`
- Name: project.task.pivot.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_pivot`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `worksheet_template_id`
- XPath or positional patches: 1

### `project_task_gantt_view_groupby_worksheet`
- Name: project.task.gantt.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.project_task_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_map_view_inherit_fsm_report2`
- Name: project.task.view.fsm.report.map2
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_map_view_inherit_fsm_report`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_map_view_inherit_fsm_report`
- Name: project.task.view.fsm.report.map
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_map_view_fsm`
- Root tag: `field`
- Field references: 2
- Sample fields: `project_id`, `worksheet_template_id`
- XPath or positional patches: 0

### `view_task_form2_inherit`
- Name: task.form.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.view_task_form2_inherit`
- Root tag: `field`
- Field references: 4
- Sample fields: `allow_worksheets`, `project_id`, `worksheet_count`, `worksheet_template_id`
- Buttons: `action_fsm_worksheet`
- XPath or positional patches: 3

### `project_task_view_search_fsm_report`
- Name: project.task.search.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_search_form_project_fsm_base`
- Root tag: `field`
- Field references: 2
- Sample fields: `project_id`, `worksheet_template_id`
- XPath or positional patches: 1

### `project_task_view_form_fsm_quick_create`
- Name: project.task.form.quick_create.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.quick_create_task_form_fsm`
- Root tag: `field`
- Field references: 3
- Sample fields: `allow_worksheets`, `user_ids`, `worksheet_template_id`
- XPath or positional patches: 0

### `project_task_view_kanban_fsm_report`
- Name: project.task.kanban.fsm.report
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_view_kanban_fsm`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `worksheet_template_id`
- XPath or positional patches: 2

### `project_task_view_calendar_fsm_worksheet`
- Name: project.task.calendar.fsm.worksheet
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_view_calendar_fsm`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `worksheet_template_id`
- XPath or positional patches: 2

### `project_task_view_gantt_fsm_worksheet`
- Name: project.task.view.gantt.fsm.worksheet
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.project_task_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `project_task_action_planning_groupby_worksheet_fsm2_view_form`: `view`
- `project_task_action_planning_groupby_worksheet_fsm2_view_graph`: `view`
- `project_task_action_planning_groupby_worksheet_fsm2_view_pivot`: `view`
- `project_task_action_fsm_planning_groupby_worksheet2_view_activity`: `view`
- `project_task_action_planning_groupby_worksheet_fsm2_view_map`: `view`
- `project_task_action_planning_groupby_worksheet_fsm2_view_calendar`: `view`
- `project_task_action_planning_groupby_worksheet_fsm2_view_list`: `view`
- `project_task_action_planning_groupby_worksheet_fsm2_view_kanban`: `view`
- `project_task_action_planning_groupby_worksheet2_gantt`: `view`
- `project_task_action_fsm_planning_groupby_worksheet2`: `act_window` Planning by Worksheet Template
- `project_task_action_planning_groupby_worksheet_fsm_view_form`: `view`
- `project_task_action_planning_groupby_worksheet_fsm_view_graph`: `view`
- `project_task_action_planning_groupby_worksheet_fsm_view_pivot`: `view`
- `project_task_action_fsm_planning_groupby_worksheet_view_activity`: `view`
- `project_task_action_planning_groupby_worksheet_fsm_view_map`: `view`
- `project_task_action_planning_groupby_worksheet_fsm_view_calendar`: `view`
- `project_task_action_planning_groupby_worksheet_fsm_view_list`: `view`
- `project_task_action_planning_groupby_worksheet_fsm_view_kanban`: `view`
- `project_task_action_planning_groupby_worksheet_gantt`: `view`
- `project_task_action_fsm_planning_groupby_worksheet`: `act_window` Planning by Worksheet Template

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_report/Views]]

<!-- GENERATED:VIEWFILE -->
