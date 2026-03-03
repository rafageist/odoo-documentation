---
tags: [odoo, community, generated, views]
---

# views/crm_lead_views.xml

- Module: [[docs/Community Addons/website_crm_iap_reveal/website_crm_iap_reveal|website_crm_iap_reveal]]
- Scope: Community Addons
- Source file: `views/crm_lead_views.xml`
- Views: 8
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `crm_opportunity_report_view_pivot_lead`
- Name: crm.opportunity.report.view.pivot.lead.inherit.website.crm.iap.reveal
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_opportunity_report_view_pivot_lead`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `reveal_iap_credits`
- XPath or positional patches: 1

### `crm_lead_view_pivot_forecast`
- Name: crm.lead.view.pivot.forecast.inherit.website.crm.iap.reveal
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_pivot_forecast`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `reveal_iap_credits`
- XPath or positional patches: 1

### `crm_lead_view_graph_report_forecast`
- Name: crm.lead.view.graph.forecast.inherit.website.crm.iap.reveal
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_graph_forecast`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `reveal_iap_credits`
- XPath or positional patches: 1

### `crm_lead_view_graph_report_lead`
- Name: crm.lead.view.graph.report.lead.inherit.lead.website
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_opportunity_report_view_graph_lead`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `reveal_iap_credits`
- XPath or positional patches: 1

### `crm_lead_view_graph_report_opportunity`
- Name: crm.lead.view.graph.report.opportunity.inherit.lead.website
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_opportunity_report_view_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `reveal_iap_credits`
- XPath or positional patches: 1

### `crm_lead_view_graph`
- Name: crm.lead.view.graph.inherit.lead.website
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `reveal_iap_credits`
- XPath or positional patches: 1

### `crm_lead_view_pivot`
- Name: crm.lead.view.pivot.inherit.lead.website
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_pivot`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `reveal_iap_credits`
- XPath or positional patches: 1

### `crm_reveal_lead_opportunity_form`
- Name: crm.lead.inherited.crm
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `reveal_iap_credits`, `reveal_ip`, `reveal_rule_id`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/website_crm_iap_reveal/Views]]

