---
tags: [odoo, community, generated, views]
---

# views/crm_team_member_views.xml

- Module: [[docs/Community Addons/sales_team/sales_team|sales_team]]
- Scope: Community Addons
- Source file: `views/crm_team_member_views.xml`
- Views: 7
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `crm_team_member_view_form_from_team`
- Name: crm.team.member.view.form.from.team
- Model: `crm.team.member`
- Type: inferred from arch
- Inherits: `sales_team.crm_team_member_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `crm_team_member_view_form`
- Name: crm.team.member.view.form
- Model: `crm.team.member`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `active`, `company_id`, `crm_team_id`, `email`, `image_1920`, `is_membership_multi`, `member_warning`, `phone`, `user_company_ids`, `user_id`, and 1 more
- Buttons: `crm_team_activate_multi_membership`
- XPath or positional patches: 0

### `crm_team_member_view_kanban_from_team`
- Name: crm.team.member.view.kanban.from.team
- Model: `crm.team.member`
- Type: inferred from arch
- Inherits: `sales_team.crm_team_member_view_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `crm_team_member_view_kanban`
- Name: crm.team.member.view.kanban
- Model: `crm.team.member`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `active`, `crm_team_id`, `email`, `user_id`
- XPath or positional patches: 0

### `crm_team_member_view_tree_from_team`
- Name: crm.team.member.view.list.from.team
- Model: `crm.team.member`
- Type: inferred from arch
- Inherits: `sales_team.crm_team_member_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `crm_team_member_view_tree`
- Name: crm.team.member.view.list
- Model: `crm.team.member`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `crm_team_id`, `user_id`
- XPath or positional patches: 0

### `crm_team_member_view_search`
- Name: crm.team.member.view.search
- Model: `crm.team.member`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `crm_team_id`, `user_id`
- XPath or positional patches: 0

## Actions

- `crm_team_member_action`: `act_window` Team Members

## Navigation

- **Parent:** [[docs/Community Addons/sales_team/Views]]

