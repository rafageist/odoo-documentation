<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Customer References

- Version: v18
- Category: community
- Source: odoo/addons/website_customer
- Dependencies: [[Odoo 18/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]], [[Odoo 18/Community Addons/website_partner/website_partner|website_partner]], [[Odoo 18/Community Addons/website_google_map/website_google_map|website_google_map]]

## Summary

Publish your customer references

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 6

## Detected Models

- `Partner`
- `res.partner.tag`
- `Website`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Customer References - Models and Relations
class Partner
class "res.partner.tag" as res_partner_tag
class Website
Partner .. res_partner_tag : many2many
class "res.partner" as res_partner
res_partner_tag .. res_partner : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
