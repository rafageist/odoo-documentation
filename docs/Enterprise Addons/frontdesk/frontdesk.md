<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Frontdesk

- Scope: Enterprise Addons
- Source: enterprise/frontdesk
- Dependencies: [[docs/Community Addons/hr/hr|hr]], [[docs/Community Addons/sms/sms|sms]]

## Summary

Visitor management system

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 6
- Views: 19
- Actions: 14
- Menus: 9
- Rules (ir.rule): 6
- Access CSV entries: 7
- Controller units: 1
- Frontend asset files: 22

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
title Frontdesk - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n19 views\n6 files" as views
component "Controllers\n11 routes" as controllers
component "Frontend\n22 files" as frontend
component "Security / Data\n6 rules\n7 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/frontdesk/Models|Models]] (3)
- Views and XML: [[docs/Enterprise Addons/frontdesk/Views|Views]] (6 files)
- Controllers: [[docs/Enterprise Addons/frontdesk/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/frontdesk/Frontend|Frontend]] (22 files)

## Key models

- `frontdesk.drink`
- `frontdesk.frontdesk`
- `frontdesk.visitor`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




