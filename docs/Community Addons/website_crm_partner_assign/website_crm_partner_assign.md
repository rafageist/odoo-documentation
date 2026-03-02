<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Resellers

- Scope: Community Addons
- Source: odoo/addons/website_crm_partner_assign
- Dependencies: [[docs/Community Addons/base_geolocalize/base_geolocalize|base_geolocalize]], [[docs/Community Addons/crm/crm|crm]], [[docs/Community Addons/account/account|account]], [[docs/Community Addons/partnership/partnership|partnership]], [[docs/Community Addons/website_partner/website_partner|website_partner]], [[docs/Community Addons/website_google_map/website_google_map|website_google_map]], [[docs/Community Addons/portal/portal|portal]]

## Summary

Publish your resellers/partners and forward leads to them

## XML Artifacts (detected)

- Views: 22
- Actions: 4
- Menus: 2
- Rules (ir.rule): 4
- Access CSV entries: 11

## Detected Models

- `CrmLead`
- `ResPartner`
- `res.partner.activation`
- `res.partner.grade`
- `Website`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Resellers - Models and Relations
class CrmLead
class ResPartner
class "res.partner.activation" as res_partner_activation
class "res.partner.grade" as res_partner_grade
class Website
class "res.partner" as res_partner
CrmLead --> res_partner : many2one
CrmLead .. res_partner : many2many
ResPartner --> res_partner_activation : many2one
ResPartner --> res_partner : many2one
ResPartner --|> res_partner : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




