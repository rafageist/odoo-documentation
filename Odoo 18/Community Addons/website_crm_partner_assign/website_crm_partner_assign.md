<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Resellers

- Version: v18
- Category: community
- Source: odoo/addons/website_crm_partner_assign
- Dependencies: [[Odoo 18/Community Addons/base_geolocalize/base_geolocalize|base_geolocalize]], [[Odoo 18/Community Addons/crm/crm|crm]], [[Odoo 18/Community Addons/account/account|account]], [[Odoo 18/Community Addons/website_partner/website_partner|website_partner]], [[Odoo 18/Community Addons/website_google_map/website_google_map|website_google_map]], [[Odoo 18/Community Addons/portal/portal|portal]]

## Summary

Publish your resellers/partners and forward leads to them

## XML Artifacts (detected)

- Views: 25
- Actions: 5
- Menus: 4
- Rules (ir.rule): 4
- Access CSV entries: 14

## Detected Models

- `CrmLead`
- `ResPartner`
- `res.partner.activation`
- `res.partner.grade`
- `Website`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Resellers - Models and Relations
class CrmLead
class ResPartner
class "res.partner.activation" as res_partner_activation
class "res.partner.grade" as res_partner_grade
class Website
class "res.partner" as res_partner
CrmLead --> res_partner : many2one
CrmLead .. res_partner : many2many
ResPartner --> res_partner_grade : many2one
ResPartner --> res_partner_activation : many2one
ResPartner --> res_partner : many2one
ResPartner --|> res_partner : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
