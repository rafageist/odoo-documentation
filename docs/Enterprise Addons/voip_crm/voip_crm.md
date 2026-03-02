<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Phone - CRM

- Scope: Enterprise Addons
- Source: enterprise/voip_crm
- Dependencies: [[docs/Community Addons/crm/crm|crm]], [[docs/Enterprise Addons/voip/voip|voip]]

## Summary

Phone integration with CRM module.

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 3
- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 17

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
title Phone - CRM - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n2 views\n3 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n17 files" as frontend
component "Security / Data\n1 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/voip_crm/Models|Models]] (4)
- Views and XML: [[docs/Enterprise Addons/voip_crm/Views|Views]] (3 files)
- Frontend: [[docs/Enterprise Addons/voip_crm/Frontend|Frontend]] (17 files)

## Key models

- `crm.lead`
- `ir.http`
- `res.partner`
- `voip.call`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





