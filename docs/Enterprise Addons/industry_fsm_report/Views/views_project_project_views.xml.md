---
tags: [odoo, enterprise, generated, views]
---

# views/project_project_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm_report/industry_fsm_report|industry_fsm_report]]
- Scope: Enterprise Addons
- Source file: `views/project_project_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_project_kanban_inherit_industry_fsm_report`
- Name: project.project.kanban.inherit.industry.fsm.report
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `worksheet_template_id`
- XPath or positional patches: 1

### `project_project_form_inherit_industry_fsm_report`
- Name: project.project.form.inherit.industry.fsm.report
- Model: `project.project`
- Type: inferred from arch
- Inherits: `industry_fsm.project_view_form_inherit`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `allow_worksheets`, `worksheet_template_id`
- XPath or positional patches: 1

## Actions

- `industry_fsm.project_project_action_only_fsm`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_report/Views]]

