<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_team_member_views.xml

- Module: [[docs/Community Addons/crm/crm|crm]]
- Scope: Community Addons
- Source file: `views/crm_team_member_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `crm_team_member_view_form`
- Name: crm.team.member.view.form.inherit.crm
- Model: `crm.team.member`
- Type: inferred from arch
- Inherits: `sales_team.crm_team_member_view_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `assignment_domain`, `assignment_domain_preferred`, `assignment_max`, `assignment_optout`, `lead_month_count`
- XPath or positional patches: 1

### `crm_team_member_view_kanban`
- Name: crm.team.member.view.kanban.inherit.crm
- Model: `crm.team.member`
- Type: inferred from arch
- Inherits: `sales_team.crm_team_member_view_kanban`
- Root tag: `field`
- Field references: 5
- Sample fields: `active`, `assignment_enabled`, `assignment_max`, `assignment_optout`, `lead_month_count`
- XPath or positional patches: 1

### `crm_team_member_view_tree`
- Name: crm.team.member.view.list
- Model: `crm.team.member`
- Type: inferred from arch
- Inherits: `sales_team.crm_team_member_view_tree`
- Root tag: `field`
- Field references: 5
- Sample fields: `assignment_enabled`, `assignment_max`, `assignment_optout`, `lead_month_count`, `user_id`
- XPath or positional patches: 0

## Actions

- `sales_team.crm_team_member_action`: `act_window`

## Navigation

- **Parent:** [[docs/Community Addons/crm/Views]]

<!-- GENERATED:VIEWFILE -->
