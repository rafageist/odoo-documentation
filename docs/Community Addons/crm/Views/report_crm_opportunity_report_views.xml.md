<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/crm_opportunity_report_views.xml

- Module: [[docs/Community Addons/crm/crm|crm]]
- Scope: Community Addons
- Source file: `report/crm_opportunity_report_views.xml`
- Views: 7
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `crm_lead_view_tree_reporting`
- Name: crm.lead.list.lead.reporting
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_tree_view_leads`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `lost_reason_id`, `stage_id`, `type`
- XPath or positional patches: 3

### `crm_opportunity_report_view_search`
- Name: crm.lead.search
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `search`
- Field references: 11
- Sample fields: `campaign_id`, `company_id`, `create_date`, `date_closed`, `date_open`, `medium_id`, `partner_id`, `source_id`, `stage_id`, `team_id`, and 1 more
- XPath or positional patches: 0

### `crm_opportunity_report_view_graph_lead`
- Name: crm.opportunity.report.graph.lead
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 10
- Sample fields: `automated_probability`, `color`, `create_date`, `message_bounce`, `probability`, `recurring_revenue`, `recurring_revenue_monthly`, `recurring_revenue_monthly_prorated`, `recurring_revenue_prorated`, `team_id`
- XPath or positional patches: 0

### `crm_opportunity_report_view_graph`
- Name: crm.opportunity.report.graph
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 11
- Sample fields: `automated_probability`, `color`, `date_deadline`, `message_bounce`, `probability`, `prorated_revenue`, `recurring_revenue`, `recurring_revenue_monthly`, `recurring_revenue_monthly_prorated`, `recurring_revenue_prorated`, and 1 more
- XPath or positional patches: 0

### `crm_opportunity_report_view_pivot_lead`
- Name: crm.opportunity.report.view.pivot.lead
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 10
- Sample fields: `automated_probability`, `color`, `create_date`, `message_bounce`, `probability`, `recurring_revenue`, `recurring_revenue_monthly`, `recurring_revenue_monthly_prorated`, `recurring_revenue_prorated`, `team_id`
- XPath or positional patches: 0

### `crm_opportunity_report_view_pivot`
- Name: crm.opportunity.report.pivot
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 11
- Sample fields: `automated_probability`, `color`, `create_date`, `message_bounce`, `probability`, `prorated_revenue`, `recurring_revenue`, `recurring_revenue_monthly`, `recurring_revenue_monthly_prorated`, `recurring_revenue_prorated`, and 1 more
- XPath or positional patches: 0

### `crm_lead_view_tree_opportunity_reporting`
- Name: crm.lead.list.opportunity.reporting
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_tree_view_oppor`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

## Actions

- `crm_opportunity_report_action_lead`: `act_window` Leads Analysis
- `crm_opportunity_report_action`: `act_window` Pipeline Analysis

## Navigation

- **Parent:** [[docs/Community Addons/crm/Views]]

<!-- GENERATED:VIEWFILE -->
