<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Barcode

- Scope: Community Addons
- Source: odoo/addons/barcodes
- Dependencies: [[docs/Community Addons/web/web|web]]

## Summary

Scan and Parse Barcodes

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 1
- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4
- Controller units: 0
- Frontend asset files: 10

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
title Barcode - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n3 views\n1 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n10 files" as frontend
component "Security / Data\n0 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/barcodes/Models|Models]] (5)
- Views and XML: [[docs/Community Addons/barcodes/Views|Views]] (1 files)
- Frontend: [[docs/Community Addons/barcodes/Frontend|Frontend]] (10 files)

## Key models

- `barcode.nomenclature`
- `barcode.rule`
- `barcodes.barcode_events_mixin`
- `ir.http`
- `res.company`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






