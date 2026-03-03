---
tags: [odoo, community, generated, views]
---

# views/crm_lead_views.xml

- Module: [[docs/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]]
- Scope: Community Addons
- Source file: `views/crm_lead_views.xml`
- Views: 13
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `crm_lead_view_kanban`
- Name: crm.lead.view.kanban.inherit.website.crm.partner.assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_kanban_view_leads`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `partner_assigned_id`
- XPath or positional patches: 1

### `crm_lead_view_graph_report_lead`
- Name: crm.lead.view.graph.report.lead.inherit.partner.assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_opportunity_report_view_graph_lead`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

### `crm_lead_view_graph_report_opportunity`
- Name: crm.lead.view.graph.report.opportunity.inherit.partner.assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_opportunity_report_view_graph`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

### `crm_lead_view_graph_forecast`
- Name: crm.lead.view.graph.forecast.inherit.website.crm.partner.assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_graph_forecast`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

### `crm_lead_view_graph`
- Name: crm.lead.view.graph.inherit.partner.assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_graph`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

### `crm_lead_view_pivot_forecast`
- Name: crm.lead.view.pivot.forecast.inherit.website.crm.partner.assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_pivot_forecast`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

### `crm_opportunity_report_view_pivot_lead`
- Name: crm.opportunity.report.view.pivot.lead.inherit.partner_assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_opportunity_report_view_pivot_lead`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

### `crm_lead_view_pivot`
- Name: crm.lead.view.pivot.inherit.partner.assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_pivot`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

### `crm_lead_partner_filter`
- Name: crm.lead.partner.filter.assigned
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.view_crm_case_leads_filter`
- Root tag: `filter`
- Field references: 2
- Sample fields: `campaign_id`, `partner_assigned_id`
- XPath or positional patches: 2

### `view_crm_lead_geo_assign_tree`
- Name: crm.lead.lead.geo_assign.list.inherit
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_tree_view_leads`
- Root tag: `field`
- Field references: 2
- Sample fields: `partner_assigned_id`, `partner_id`
- XPath or positional patches: 0

### `crm_opportunity_partner_filter`
- Name: crm.opportunity.partner.filter.assigned
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.view_crm_case_opportunities_filter`
- Root tag: `filter`
- Field references: 2
- Sample fields: `partner_assigned_id`, `phone_mobile_search`
- XPath or positional patches: 2

### `view_crm_opportunity_geo_assign_tree`
- Name: crm.lead.geo_assign.list.inherit
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_tree_view_oppor`
- Root tag: `field`
- Field references: 3
- Sample fields: `date_partner_assign`, `partner_assigned_id`, `priority`
- XPath or positional patches: 0

### `view_crm_lead_opportunity_geo_assign_form`
- Name: crm.lead.geo_assign.inherit
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `partner_assigned_id`, `partner_latitude`, `partner_longitude`
- Buttons: `%(crm_lead_forward_to_partner_act)d`, `action_assign_partner`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_crm_partner_assign/Views]]

