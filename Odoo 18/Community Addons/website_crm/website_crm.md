<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Contact Form

- Version: v18
- Category: community
- Source: odoo/addons/website_crm
- Dependencies: [[Odoo 18/Community Addons/website/website|website]], [[Odoo 18/Community Addons/crm/crm|crm]]

## Summary

Generate leads from a contact form

## XML Artifacts (detected)

- Views: 5
- Actions: 3
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `Lead`
- `Website`
- `WebsiteVisitor`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Contact Form - Models and Relations
class Lead
class Website
class WebsiteVisitor
class "website.visitor" as website_visitor
Lead .. website_visitor : many2many
class "crm.team" as crm_team
Website --> crm_team : many2one
class "res.users" as res_users
Website --> res_users : many2one
class "crm.lead" as crm_lead
WebsiteVisitor .. crm_lead : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
