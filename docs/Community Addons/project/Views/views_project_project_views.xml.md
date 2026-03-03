---
tags: [odoo, community, generated, views]
---

# views/project_project_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `views/project_project_views.xml`
- Views: 20
- Actions: 11
- Menus: 0
- Rules: 0

## View records

### `project_templates_view_kanban`
- Name: project.project.template.kanban
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project_kanban`
- Root tag: `kanban`
- Field references: 0
- XPath or positional patches: 2

### `project_templates_view_list`
- Name: project.project.template.list
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project`
- Root tag: `list`
- Field references: 4
- Sample fields: `milestone_progress`, `next_milestone_id`, `partner_id`, `sequence`
- XPath or positional patches: 1

### `project_templates_view_form`
- Name: project.project.template.form
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.edit_project`
- Root tag: `form`
- Field references: 0
- XPath or positional patches: 1

### `project_view_kanban_inherit_project`
- Name: project.kanban.inherit.project
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `id`
- XPath or positional patches: 2

### `view_project_calendar`
- Name: project.project.calendar
- Model: `project.project`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 8
- Sample fields: `is_favorite`, `last_update_color`, `last_update_status`, `partner_id`, `stage_id`, `stage_id_color`, `tag_ids`, `user_id`
- XPath or positional patches: 0

### `view_project_config_kanban_group_stage`
- Name: project.kanban.inherit.config.project.group.stage
- Model: `project.project`
- Type: inferred from arch
- Inherits: `view_project_config_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_project_config_kanban`
- Name: project.kanban.inherit.config.project
- Model: `project.project`
- Type: inferred from arch
- Inherits: `view_project_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_kanban_view_group_stage`
- Name: project.project.kanban.group.stage
- Model: `project.project`
- Type: inferred from arch
- Inherits: `view_project_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_project_kanban`
- Name: project.project.kanban
- Model: `project.project`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 23
- Sample fields: `activity_ids`, `alias_email`, `allow_milestones`, `can_mark_milestone_as_done`, `color`, `date_start`, `display_name`, `is_favorite`, `is_milestone_deadline_exceeded`, `is_template`, and 13 more
- XPath or positional patches: 0

### `project_project_view_form_simplified_footer`
- Name: project.project.view.form.simplified
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.project_project_view_form_simplified`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_view_tasks`
- XPath or positional patches: 1

### `project_project_view_form_simplified`
- Name: project.project.view.form.simplified
- Model: `project.project`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `alias_domain_id`, `alias_id`, `alias_name`, `name`, `user_id`
- XPath or positional patches: 0

### `project_view_kanban`
- Name: project.project.kanban
- Model: `project.project`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `name`, `partner_id`, `user_id`
- XPath or positional patches: 0

### `quick_create_project_form`
- Name: project.form.quick_create
- Model: `project.project`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_project_config_group_stage`
- Name: project.project.list.config.group.stage
- Model: `project.project`
- Type: inferred from arch
- Inherits: `view_project_config`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `view_project_config`
- Name: project.project.list.config
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sequence`
- XPath or positional patches: 1

### `project_list_view_group_stage`
- Name: project.project.list.group.stage
- Model: `project.project`
- Type: inferred from arch
- Inherits: `view_project`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `view_project`
- Name: project.project.list
- Model: `project.project`
- Type: inferred from arch
- Root tag: `list`
- Field references: 21
- Sample fields: `active`, `allow_milestones`, `can_mark_milestone_as_done`, `company_id`, `date`, `date_start`, `is_favorite`, `is_milestone_deadline_exceeded`, `is_milestone_exceeded`, `last_update_color`, and 11 more
- Buttons: `action_view_tasks`
- XPath or positional patches: 0

### `view_project_project_filter`
- Name: project.project.select
- Model: `project.project`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `activity_type_id`, `activity_user_id`, `name`, `partner_id`, `stage_id`, `tag_ids`, `user_id`
- XPath or positional patches: 0

### `edit_project`
- Name: project.project.form
- Model: `project.project`
- Type: inferred from arch
- Root tag: `form`
- Field references: 30
- Sample fields: `access_instruction_message`, `account_id`, `active`, `alias_contact`, `alias_domain_id`, `alias_email`, `alias_id`, `alias_name`, `allow_milestones`, `allow_recurring_tasks`, and 20 more
- Buttons: `action_open_share_project_wizard`, `action_view_tasks`, `project_update_all_action`
- XPath or positional patches: 0

### `project_project_view_activity`
- Name: project.project.view.activity
- Model: `project.project`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 2
- Sample fields: `name`, `user_id`
- XPath or positional patches: 0

## Actions

- `action_server_convert_project_to_template`: `server` Convert to Template
- `open_view_project_all_config_group_stage_kanban_action_view`: `view`
- `open_view_project_all_config_group_stage_tree_action_view`: `view`
- `open_view_project_all_config_group_stage`: `act_window` Projects
- `open_view_project_all_config`: `act_window` Projects
- `open_view_project_all_group_stage_tree_view`: `view`
- `open_view_project_all_group_stage_kanban_view`: `view`
- `open_view_project_all_group_stage`: `act_window` Projects
- `open_view_project_all`: `act_window` Projects
- `open_create_project`: `act_window` Create a Project
- `action_send_mail_project_project`: `act_window` Send Email

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

