<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Lead Generation From Website Visits

- Version: v18
- Category: community
- Source: odoo/addons/website_crm_iap_reveal
- Dependencies: [[Odoo 18/Community Addons/iap_crm/iap_crm|iap_crm]], [[Odoo 18/Community Addons/iap_mail/iap_mail|iap_mail]], [[Odoo 18/Community Addons/crm_iap_mine/crm_iap_mine|crm_iap_mine]], [[Odoo 18/Community Addons/website_crm/website_crm|website_crm]]

## Summary

Generate Leads/Opportunities from your website's traffic

## XML Artifacts (detected)

- Views: 14
- Actions: 2
- Menus: 2
- Rules (ir.rule): 4
- Access CSV entries: 4

## Detected Models

- `Lead`
- `crm.reveal.rule`
- `crm.reveal.view`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Lead Generation From Website Visits - Models and Relations
class Lead
class "crm.reveal.rule" as crm_reveal_rule
class "crm.reveal.view" as crm_reveal_view
Lead --> crm_reveal_rule : many2one
class "res.country" as res_country
crm_reveal_rule .. res_country : many2many
class website
crm_reveal_rule --> website : many2one
class "res.country.state" as res_country_state
crm_reveal_rule .. res_country_state : many2many
class "crm.iap.lead.industry" as crm_iap_lead_industry
crm_reveal_rule .. crm_iap_lead_industry : many2many
class "crm.iap.lead.role" as crm_iap_lead_role
crm_reveal_rule --> crm_iap_lead_role : many2one
crm_reveal_rule .. crm_iap_lead_role : many2many
class "crm.iap.lead.seniority" as crm_iap_lead_seniority
crm_reveal_rule --> crm_iap_lead_seniority : many2one
class "crm.team" as crm_team
crm_reveal_rule --> crm_team : many2one
class "crm.tag" as crm_tag
crm_reveal_rule .. crm_tag : many2many
class "res.users" as res_users
crm_reveal_rule --> res_users : many2one
class "crm.lead" as crm_lead
crm_reveal_rule --|> crm_lead : one2many
crm_reveal_view --> crm_reveal_rule : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
