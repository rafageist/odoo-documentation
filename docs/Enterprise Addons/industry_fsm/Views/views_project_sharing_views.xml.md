<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/project_sharing_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]]
- Scope: Enterprise Addons
- Source file: `views/project_sharing_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `project_sharing_project_task_view_search_inherit`
- Name: project.sharing.task.search.form.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

### `project_sharing_inherit_project_task_view_form`
- Name: project.sharing.project.task.view.form.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_form`
- Root tag: `xpath`
- Field references: 11
- Sample fields: `allocated_hours`, `date_deadline`, `is_fsm`, `partner_id`, `progress`, `recurring_task`, `repeat_interval`, `repeat_type`, `repeat_unit`, `repeat_until`, and 1 more
- XPath or positional patches: 12

### `project_sharing_quick_create_task_form_inherit`
- Name: project.sharing.form.quick_create.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_quick_create_task_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `company_id`, `is_fsm`, `partner_id`, `project_id`
- XPath or positional patches: 1

### `project_sharing_project_task_inherit_view_kanban`
- Name: project.sharing.project.task.view.kanban.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_kanban`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `fsm_done`, `is_fsm`, `partner_city`, `planned_date_begin`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm/Views]]

<!-- GENERATED:VIEWFILE -->
