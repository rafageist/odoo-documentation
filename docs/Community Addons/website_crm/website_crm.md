<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Contact Form

- Scope: Community Addons
- Source: odoo/addons/website_crm
- Dependencies: [[docs/Community Addons/website/website|website]], [[docs/Community Addons/crm/crm|crm]]

## Summary

Generate leads from a contact form

## XML Artifacts (detected)

- Views: 5
- Actions: 3
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `CrmLead`
- `Website`
- `WebsiteVisitor`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Contact Form - Models and Relations
class CrmLead
class Website
class WebsiteVisitor
class "website.visitor" as website_visitor
CrmLead .. website_visitor : many2many
class "crm.team" as crm_team
Website --> crm_team : many2one
class "res.users" as res_users
Website --> res_users : many2one
class "crm.lead" as crm_lead
WebsiteVisitor .. crm_lead : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



