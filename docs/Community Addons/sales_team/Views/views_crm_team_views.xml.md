<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_team_views.xml

- Module: [[docs/Community Addons/sales_team/sales_team|sales_team]]
- Scope: Community Addons
- Source file: `views/crm_team_views.xml`
- Views: 5
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `crm_team_view_kanban_dashboard`
- Name: crm.team.view.kanban.dashboard
- Model: `crm.team`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `color`, `company_id`, `name`, `user_id`
- XPath or positional patches: 0

### `crm_team_view_kanban`
- Name: crm.team.view.kanban
- Model: `crm.team`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `name`, `user_id`
- XPath or positional patches: 0

### `crm_team_view_tree`
- Name: crm.team.list
- Model: `crm.team`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `active`, `company_id`, `name`, `sequence`, `user_id`
- XPath or positional patches: 0

### `crm_team_view_form`
- Name: crm.team.form
- Model: `crm.team`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `active`, `avatar_128`, `company_id`, `crm_team_member_ids`, `currency_id`, `email`, `is_membership_multi`, `member_company_ids`, `member_ids`, `member_warning`, and 3 more
- Buttons: `crm_team_activate_multi_membership`
- XPath or positional patches: 0

### `crm_team_view_search`
- Name: crm.team.view.search
- Model: `crm.team`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `member_ids`, `name`, `user_id`
- XPath or positional patches: 0

## Actions

- `crm_team_action_config`: `act_window` Sales Teams
- `crm_team_action_pipeline`: `act_window` Teams
- `crm_team_action_sales`: `act_window` Sales Teams

## Navigation

- **Parent:** [[docs/Community Addons/sales_team/Views]]

<!-- GENERATED:VIEWFILE -->
