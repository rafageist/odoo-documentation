<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Website Appointments

- Scope: Enterprise Addons
- Source: enterprise/website_appointment
- Dependencies: [[docs/Enterprise Addons/appointment/appointment|appointment]], [[docs/Enterprise Addons/website_enterprise/website_enterprise|website_enterprise]], [[docs/Community Addons/website_partner/website_partner|website_partner]], [[docs/Community Addons/html_builder/html_builder|html_builder]]

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 6
- Views: 10
- Actions: 2
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 2
- Controller units: 3
- Frontend asset files: 19

## Module map

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title Website Appointments - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n10 views\n6 files" as views
component "Controllers\n4 routes" as controllers
component "Frontend\n19 files" as frontend
component "Security / Data\n1 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/website_appointment/Models|Models]] (6)
- Views and XML: [[docs/Enterprise Addons/website_appointment/Views|Views]] (6 files)
- Controllers: [[docs/Enterprise Addons/website_appointment/Controllers|Controllers]] (3)
- Frontend: [[docs/Enterprise Addons/website_appointment/Frontend|Frontend]] (19 files)

## Key models

- `appointment.invite`
- `appointment.type`
- `calendar.event`
- `website`
- `website.snippet.filter`
- `website.visitor`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




