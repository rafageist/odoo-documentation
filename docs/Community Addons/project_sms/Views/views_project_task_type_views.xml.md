---
tags: [odoo, community, generated, views]
---

# views/project_task_type_views.xml

- Module: [[docs/Community Addons/project_sms/project_sms|project_sms]]
- Scope: Community Addons
- Source file: `views/project_task_type_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `task_type_search_view_search_inherit_project_sms`
- Name: project.task.type.view.search.inherit.project.sms
- Model: `project.task.type`
- Type: inferred from arch
- Inherits: `project.task_type_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `rating_template_id`, `sms_template_id`
- XPath or positional patches: 0

### `task_type_edit_view_tree_inherit_project_sms`
- Name: project.task.type.view.list.inherit.project.sms
- Model: `project.task.type`
- Type: inferred from arch
- Inherits: `project.task_type_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `mail_template_id`, `sms_template_id`
- XPath or positional patches: 0

### `task_type_edit_view_form_inherit_project_sms`
- Name: project.task.type.view.form.inherit.project.sms
- Model: `project.task.type`
- Type: inferred from arch
- Inherits: `project.task_type_edit`
- Root tag: `field`
- Field references: 2
- Sample fields: `mail_template_id`, `sms_template_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/project_sms/Views]]

