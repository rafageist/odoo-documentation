<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Recruitment tracking on appointments

- Version: v18
- Category: enterprise
- Source: enterprise18/appointment_hr_recruitment
- Dependencies: [[Odoo 18/Enterprise Addons/appointment/appointment|appointment]], [[Odoo 18/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]

## Summary

Keep track of recruitment appointments

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AppointmentInviteHrRecruitment`
- `AppointmentType`
- `CalendarEventRecruitment`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Recruitment tracking on appointments - Models and Relations
class AppointmentInviteHrRecruitment
class AppointmentType
class CalendarEventRecruitment
class "hr.applicant" as hr_applicant
AppointmentInviteHrRecruitment --> hr_applicant : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
