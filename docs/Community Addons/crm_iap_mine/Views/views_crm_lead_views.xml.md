<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_lead_views.xml

- Module: [[docs/Community Addons/crm_iap_mine/crm_iap_mine|crm_iap_mine]]
- Scope: Community Addons
- Source file: `views/crm_lead_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `crm_case_kanban_view_leads`
- Name: crm.lead.kanban.lead.inherit.iap.mine
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_kanban_view_leads`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_generate_leads`
- XPath or positional patches: 1

### `view_crm_lead_kanban`
- Name: crm.lead.kanban.inherit.iap.mine
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.view_crm_lead_kanban`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_generate_leads`
- XPath or positional patches: 1

### `crm_lead_view_tree_lead`
- Name: crm.lead.view.list.lead.inherit.iap.mine
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_tree_view_leads`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_generate_leads`
- XPath or positional patches: 1

### `crm_lead_view_tree_opportunity`
- Name: crm.lead.view.list.opportunity.inherit.iap.mine
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_tree_view_oppor`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_generate_leads`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/crm_iap_mine/Views]]

<!-- GENERATED:VIEWFILE -->
