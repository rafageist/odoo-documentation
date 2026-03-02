<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/crm_lead_views.xml

- Module: [[docs/Enterprise Addons/crm_enterprise/crm_enterprise|crm_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/crm_lead_views.xml`
- Views: 8
- Actions: 9
- Menus: 1
- Rules: 0

## View records

### `crm_lead_view_cohort`
- Name: crm.lead.view.cohort
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `cohort`
- Field references: 9
- Sample fields: `automated_probability`, `color`, `message_bounce`, `probability`, `recurring_revenue`, `recurring_revenue_monthly`, `recurring_revenue_monthly_prorated`, `recurring_revenue_prorated`, `stage_id_color`
- XPath or positional patches: 0

### `crm_lead_view_map`
- Name: crm.lead.view.map
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `map`
- Field references: 1
- Sample fields: `partner_id`
- XPath or positional patches: 0

### `crm_lead_view_graph_forecast`
- Name: crm.lead.view.graph.forecast.inherit
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_graph_forecast`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `days_to_convert`
- XPath or positional patches: 1

### `crm_lead_view_graph`
- Name: crm.lead.graph.view
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 10
- Sample fields: `automated_probability`, `color`, `create_date`, `message_bounce`, `probability`, `recurring_revenue`, `recurring_revenue_monthly`, `recurring_revenue_monthly_prorated`, `recurring_revenue_prorated`, `stage_id_color`
- XPath or positional patches: 0

### `crm_lead_view_pivot_forecast`
- Name: crm.lead.view.pivot.forecast.inherit
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_pivot_forecast`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `days_to_convert`
- XPath or positional patches: 1

### `crm_lead_view_pivot`
- Name: crm.lead.pivot.view
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 13
- Sample fields: `automated_probability`, `color`, `day_close`, `expected_revenue`, `message_bounce`, `probability`, `prorated_revenue`, `recurring_revenue`, `recurring_revenue_monthly`, `recurring_revenue_monthly_prorated`, and 3 more
- XPath or positional patches: 0

### `crm_opportunity_view_graph`
- Name: crm.lead.graph.view
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 11
- Sample fields: `automated_probability`, `color`, `date_deadline`, `message_bounce`, `probability`, `recurring_revenue`, `recurring_revenue_monthly`, `recurring_revenue_monthly_prorated`, `recurring_revenue_prorated`, `stage_id`, and 1 more
- XPath or positional patches: 0

### `crm_lead_view_list_opportunities`
- Name: crm.lead.view.list.opportunities.inherit.business.cards
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_tree_view_oppor`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `crm.crm_opportunity_report_action_lead`: `act_window`
- `crm_opportunity_partner_add_cohort`: `view`
- `crm_lead_action_pipeline_view_map`: `view`
- `crm_opportunity_action_dashboard_tree`: `view`
- `crm_opportunity_action_dashboard_cohort`: `view`
- `crm_opportunity_action_dashboard_graph`: `view`
- `crm_opportunity_action_dashboard_pivot`: `view`
- `crm_opportunity_action_dashboard`: `act_window` Pipeline Analysis
- `crm.action_report_crm_lead_salesteam`: `act_window`

## Menus

- `crm.crm_opportunity_report_menu`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/crm_enterprise/Views]]

<!-- GENERATED:VIEWFILE -->
