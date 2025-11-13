<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Event CRM

- Version: v19
- Category: community
- Source: odoo19/addons/event_crm
- Dependencies: [[Odoo 19/Community Addons/event/event|event]], [[Odoo 19/Community Addons/crm/crm|crm]]
## XML Artifacts (detected)

- Views: 8
- Actions: 6
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 5

## Detected Models

- `CrmLead`
- `EventEvent`
- `event.lead.request`
- `event.lead.rule`
- `EventQuestionAnswer`
- `EventRegistration`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Event CRM - Models and Relations
class CrmLead
class EventEvent
class "event.lead.request" as event_lead_request
class "event.lead.rule" as event_lead_rule
class EventQuestionAnswer
class EventRegistration
CrmLead --> event_lead_rule : many2one
class "event.event" as event_event
CrmLead --> event_event : many2one
class "event.registration" as event_registration
CrmLead .. event_registration : many2many
class "crm.lead" as crm_lead
EventEvent --|> crm_lead : one2many
event_lead_request --> event_event : many2one
event_lead_request .. event_lead_rule : many2many
event_lead_rule --|> crm_lead : one2many
class "event.type" as event_type
event_lead_rule .. event_type : many2many
event_lead_rule --> event_event : many2one
class "res.company" as res_company
event_lead_rule --> res_company : many2one
class "crm.team" as crm_team
event_lead_rule --> crm_team : many2one
class "res.users" as res_users
event_lead_rule --> res_users : many2one
class "crm.tag" as crm_tag
event_lead_rule .. crm_tag : many2many
EventRegistration .. crm_lead : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
