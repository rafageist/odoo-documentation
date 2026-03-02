<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_team_views.xml

- Module: [[docs/Community Addons/crm/crm|crm]]
- Scope: Community Addons
- Source file: `views/crm_team_views.xml`
- Views: 3
- Actions: 12
- Menus: 0
- Rules: 0

## View records

### `crm_team_view_kanban_dashboard`
- Name: crm.team.view.kanban.dashboard.inherit.crm
- Model: `crm.team`
- Type: inferred from arch
- Inherits: `sales_team.crm_team_view_kanban_dashboard`
- Root tag: `data`
- Field references: 6
- Sample fields: `alias_domain`, `alias_id`, `alias_name`, `lead_unassigned_count`, `use_leads`, `use_opportunities`
- XPath or positional patches: 10

### `sales_team_form_view_in_crm`
- Name: crm.team.form.inherit
- Model: `crm.team`
- Type: inferred from arch
- Inherits: `sales_team.crm_team_view_form`
- Root tag: `xpath`
- Field references: 13
- Sample fields: `alias_contact`, `alias_domain_id`, `alias_id`, `alias_name`, `assignment_auto_enabled`, `assignment_domain`, `assignment_enabled`, `assignment_max`, `assignment_optout`, `lead_all_assigned_month_count`, and 3 more
- Buttons: `action_assign_leads`
- XPath or positional patches: 7

### `crm_team_view_tree`
- Name: crm.team.list.inherit.crm
- Model: `crm.team`
- Type: inferred from arch
- Inherits: `sales_team.crm_team_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `alias_id`, `name`
- XPath or positional patches: 0

## Actions

- `sales_team.crm_team_action_pipeline`: `act_window`
- `action_opportunity_form`: `act_window` New Opportunity
- `action_crm_tag_tree_view_salesteams_oppor11`: `view`
- `action_crm_tag_kanban_view_salesteams_oppor11`: `view`
- `action_report_crm_opportunity_salesteam`: `act_window` Pipeline Analysis
- `action_report_crm_lead_salesteam_view_tree`: `view`
- `action_report_crm_lead_salesteam_view_pivot`: `view`
- `action_report_crm_lead_salesteam_view_graph`: `view`
- `action_report_crm_lead_salesteam`: `act_window` Leads Analysis
- `crm_lead_action_team_overdue_opportunity`: `act_window` Overdue Opportunities
- `crm_case_form_view_salesteams_opportunity`: `act_window` Opportunities
- `crm_case_form_view_salesteams_lead`: `act_window` Leads

## Navigation

- **Parent:** [[docs/Community Addons/crm/Views]]

<!-- GENERATED:VIEWFILE -->
