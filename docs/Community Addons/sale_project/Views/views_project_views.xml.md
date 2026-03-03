---
tags: [odoo, community, generated, views]
---

# views/project_views.xml

- Module: [[docs/Community Addons/sale_project/sale_project|sale_project]]
- Scope: Community Addons
- Source file: `views/project_views.xml`
- Views: 2
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `project_templates_view_list`
- Name: project.project.template.list
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.project_templates_view_list`
- Root tag: `field`
- Field references: 1
- Sample fields: `sale_line_id`
- XPath or positional patches: 0

### `project_project_view_form_simplified_inherit`
- Name: project.project.view.form.simplified.inherit
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.project_project_view_form_simplified`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `allow_billable`, `company_id`, `partner_id`
- XPath or positional patches: 1

## Actions

- `project.open_view_project_all_group_stage`: `act_window`
- `project.open_view_project_all`: `act_window`
- `project.open_view_project_all_config_group_stage`: `act_window`
- `project.open_view_project_all_config`: `act_window`

## Navigation

- **Parent:** [[docs/Community Addons/sale_project/Views]]

