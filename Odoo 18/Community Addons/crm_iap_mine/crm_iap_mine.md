<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Lead Generation

- Version: v18
- Category: community
- Source: odoo/addons/crm_iap_mine
- Dependencies: [[Odoo 18/Community Addons/iap_crm/iap_crm|iap_crm]], [[Odoo 18/Community Addons/iap_mail/iap_mail|iap_mail]]

## Summary

Generate Leads/Opportunities based on country, industries, size, etc.

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 5

## Detected Models

- `crm.iap.lead.helpers`
- `crm.iap.lead.industry`
- `crm.iap.lead.mining.request`
- `crm.iap.lead.role`
- `crm.iap.lead.seniority`
- `Lead`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Lead Generation - Models and Relations
class "crm.iap.lead.helpers" as crm_iap_lead_helpers
class "crm.iap.lead.industry" as crm_iap_lead_industry
class "crm.iap.lead.mining.request" as crm_iap_lead_mining_request
class "crm.iap.lead.role" as crm_iap_lead_role
class "crm.iap.lead.seniority" as crm_iap_lead_seniority
class Lead
class "crm.team" as crm_team
crm_iap_lead_mining_request --> crm_team : many2one
class "res.users" as res_users
crm_iap_lead_mining_request --> res_users : many2one
class "crm.tag" as crm_tag
crm_iap_lead_mining_request .. crm_tag : many2many
class "crm.lead" as crm_lead
crm_iap_lead_mining_request --|> crm_lead : one2many
class "res.country" as res_country
crm_iap_lead_mining_request .. res_country : many2many
class "res.country.state" as res_country_state
crm_iap_lead_mining_request .. res_country_state : many2many
crm_iap_lead_mining_request --|> res_country_state : one2many
crm_iap_lead_mining_request .. crm_iap_lead_industry : many2many
crm_iap_lead_mining_request --> crm_iap_lead_role : many2one
crm_iap_lead_mining_request .. crm_iap_lead_role : many2many
crm_iap_lead_mining_request --> crm_iap_lead_seniority : many2one
Lead --> crm_iap_lead_mining_request : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
