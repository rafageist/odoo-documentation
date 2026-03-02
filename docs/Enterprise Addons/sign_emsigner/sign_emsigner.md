<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sign emSigner

- Scope: Enterprise Addons
- Source: enterprise/sign_emsigner
- Dependencies: [[docs/Enterprise Addons/sign/sign|sign]], [[docs/Community Addons/iap/iap|iap]]

## Summary

Sign documents with emSigner

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 0
- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
- Frontend asset files: 5

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
title Sign emSigner - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n0 views\n0 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n5 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/sign_emsigner/Models|Models]] (4)
- Controllers: [[docs/Enterprise Addons/sign_emsigner/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/sign_emsigner/Frontend|Frontend]] (5 files)

## Key models

- `sign.item.role`
- `sign.request`
- `sign.request.item`
- `sign.send.request`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




