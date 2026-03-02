<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Appointment Lead Generation

- Scope: Enterprise Addons
- Source: enterprise/appointment_crm
- Dependencies: [[docs/Enterprise Addons/appointment/appointment|appointment]], [[docs/Community Addons/crm/crm|crm]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



