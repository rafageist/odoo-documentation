<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/crm_lead_views.xml

- Module: [[docs/Enterprise Addons/crm_enterprise_partner_assign/crm_enterprise_partner_assign|crm_enterprise_partner_assign]]
- Scope: Enterprise Addons
- Source file: `views/crm_lead_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `crm_lead_view_graph`
- Name: crm.lead.view.graph.inherit.partner.assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm_enterprise.crm_lead_view_graph`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

### `crm_lead_view_graph_opportunity`
- Name: crm.lead.view.graph.opportunity.inherit.partner.assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm_enterprise.crm_opportunity_view_graph`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

### `crm_lead_view_cohort`
- Name: crm.lead.view.cohort.inherit.partner.assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm_enterprise.crm_lead_view_cohort`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

### `crm_lead_view_pivot`
- Name: crm.lead.view.pivot.inherit.partner.assign
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm_enterprise.crm_lead_view_pivot`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/crm_enterprise_partner_assign/Views]]

<!-- GENERATED:VIEWFILE -->
