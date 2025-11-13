<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Website Appointments

- Version: v19
- Category: enterprise
- Source: enterprise19/website_appointment
- Dependencies: [[Odoo 19/Enterprise Addons/appointment/appointment|appointment]], [[Odoo 19/Enterprise Addons/website_enterprise/website_enterprise|website_enterprise]], [[Odoo 19/Community Addons/website_partner/website_partner|website_partner]], [[Odoo 19/Community Addons/html_builder/html_builder|html_builder]]
## XML Artifacts (detected)

- Views: 10
- Actions: 2
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `appointment.invite`
- `appointment.type`
- `CalendarEvent`
- `Website`
- `WebsiteSnippetFilter`
- `WebsiteVisitor`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website Appointments - Models and Relations
class "appointment.invite" as appointment_invite
class "appointment.type" as appointment_type
class CalendarEvent
class Website
class WebsiteSnippetFilter
class WebsiteVisitor
class "website.visitor" as website_visitor
CalendarEvent --> website_visitor : many2one
class "calendar.event" as calendar_event
WebsiteVisitor --|> calendar_event : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
