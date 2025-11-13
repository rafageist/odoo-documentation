<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Customer References

- Version: v19
- Category: community
- Source: odoo19/addons/website_customer
- Dependencies: [[Odoo 19/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]], [[Odoo 19/Community Addons/website_partner/website_partner|website_partner]], [[Odoo 19/Community Addons/website_google_map/website_google_map|website_google_map]]

## Summary

Publish your customer references

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 6

## Detected Models

- `ResPartner`
- `res.partner.tag`
- `Website`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Customer References - Models and Relations
class ResPartner
class "res.partner.tag" as res_partner_tag
class Website
ResPartner .. res_partner_tag : many2many
class "res.partner" as res_partner
res_partner_tag .. res_partner : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
