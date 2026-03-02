<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/project_project_stage_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `views/project_project_stage_views.xml`
- Views: 5
- Actions: 5
- Menus: 0
- Rules: 0

## View records

### `project_project_stage_view_search`
- Name: project.project.stage.view.search
- Model: `project.project.stage`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `company_id`, `mail_template_id`, `name`
- XPath or positional patches: 0

### `project_project_stage_view_kanban`
- Name: project.project.stage.view.kanban
- Model: `project.project.stage`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `color`, `company_id`, `mail_template_id`, `name`
- XPath or positional patches: 0

### `project_project_stage_view_form`
- Name: project.project.stage.view.form
- Model: `project.project.stage`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `active`, `color`, `company_id`, `fold`, `mail_template_id`, `name`, `sequence`
- XPath or positional patches: 0

### `project_project_stage_view_form_quick_create`
- Name: project.project.stage.view.form.quick.create
- Model: `project.project.stage`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `fold`, `mail_template_id`, `name`
- XPath or positional patches: 0

### `project_project_stage_view_tree`
- Name: project.project.stage.view.list
- Model: `project.project.stage`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `color`, `company_id`, `fold`, `mail_template_id`, `name`, `sequence`
- XPath or positional patches: 0

## Actions

- `unlink_project_stage_action`: `server` Delete
- `project_project_stage_configure_view_form`: `view`
- `project_project_stage_configure_view_kanban`: `view`
- `project_project_stage_configure_view_tree`: `view`
- `project_project_stage_configure`: `act_window` Project Stages

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

<!-- GENERATED:VIEWFILE -->
