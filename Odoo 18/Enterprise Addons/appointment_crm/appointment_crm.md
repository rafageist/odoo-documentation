<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Appointment Lead Generation

- Version: v18
- Category: enterprise
- Source: enterprise18/appointment_crm
- Dependencies: [[Odoo 18/Enterprise Addons/appointment/appointment|appointment]], [[Odoo 18/Community Addons/crm/crm|crm]]

## Summary

Generate leads when prospects schedule appointments

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AppointmentInviteCrm`
- `AppointmentType`
- `CalendarEventCrm`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Appointment Lead Generation - Models and Relations
class AppointmentInviteCrm
class AppointmentType
class CalendarEventCrm
class "crm.lead" as crm_lead
AppointmentInviteCrm --> crm_lead : many2one
AppointmentType .. crm_lead : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
