<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Appointment Lead Generation

- Version: v19
- Category: enterprise
- Source: enterprise19/appointment_crm
- Dependencies: [[Odoo 19/Enterprise Addons/appointment/appointment|appointment]], [[Odoo 19/Community Addons/crm/crm|crm]]

## Summary

Generate leads when prospects schedule appointments

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AppointmentInvite`
- `AppointmentType`
- `CalendarEvent`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Appointment Lead Generation - Models and Relations
class AppointmentInvite
class AppointmentType
class CalendarEvent
class "crm.lead" as crm_lead
AppointmentInvite --> crm_lead : many2one
AppointmentType .. crm_lead : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
