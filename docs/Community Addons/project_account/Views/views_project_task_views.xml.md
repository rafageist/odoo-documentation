---
tags: [odoo, community, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Community Addons/project_account/project_account|project_account]]
- Scope: Community Addons
- Source file: `views/project_task_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `project_task_tree_view_account_inherit`
- Name: project.task.list.view.account.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_task_view_tree_base`
- Root tag: `field`
- Field references: 1
- Sample fields: `partner_id`
- XPath or positional patches: 0

### `project_task_form_view_account_inherit`
- Name: project.task.form.view.account.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_form2`
- Root tag: `field`
- Field references: 1
- Sample fields: `partner_id`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/project_account/Views]]

