---
tags: [odoo, enterprise, generated, views]
---

# views/databases_project_views.xml

- Module: [[docs/Enterprise Addons/databases/databases|databases]]
- Scope: Enterprise Addons
- Source file: `views/databases_project_views.xml`
- Views: 2
- Actions: 7
- Menus: 0
- Rules: 0

## View records

### `edit_project`
- Name: databases.project.form
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.edit_project`
- Root tag: `header`
- Field references: 15
- Sample fields: `database_api_key`, `database_api_login`, `database_fetch_documents`, `database_fetch_draft_entries`, `database_fetch_tax_returns`, `database_hosting`, `database_kpi_properties`, `database_last_synchro`, `database_name`, `database_url`, and 5 more
- Buttons: `action_database_synchronize`, `action_invite_users`, `action_remove_users`
- XPath or positional patches: 2

### `view_databases_list`
- Name: databases.project.list
- Model: `project.project`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `database_kpi_properties`, `database_last_synchro`, `database_name`, `database_nb_documents`, `database_nb_users`, `database_version`, `name`, `tag_ids`, `user_id`
- Buttons: `%(databases.action_invite_users)d`, `%(databases.action_remove_users)d`, `action_database_connect`, `action_open_self`, `databases.action_synchronize_all_databases`
- XPath or positional patches: 0

## Actions

- `action_databases_configuration`: `act_window` Settings
- `action_view_tasks_all`: `act_window` Tasks
- `action_view_databases_all`: `act_window` Databases
- `action_remove_users`: `server` Remove Users
- `action_invite_users`: `server` Invite Users
- `action_synchronize_database`: `server` Synchronize
- `action_synchronize_all_databases`: `server` Synchronize all the Databases

## Navigation

- **Parent:** [[docs/Enterprise Addons/databases/Views]]

