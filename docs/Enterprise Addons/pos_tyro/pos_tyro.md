<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# POS Tyro

- Scope: Enterprise Addons
- Source: enterprise/pos_tyro
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Integrate your POS with a Tyro payment terminal (AU)

## Generated coverage

- Models: 2
- XML files with UI/data artifacts: 1
- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 20

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
title POS Tyro - Generated Coverage
component "Module Overview" as overview
component "Models\n2" as models
component "Views / XML\n1 views\n1 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n20 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/pos_tyro/Models|Models]] (2)
- Views and XML: [[docs/Enterprise Addons/pos_tyro/Views|Views]] (1 files)
- Frontend: [[docs/Enterprise Addons/pos_tyro/Frontend|Frontend]] (20 files)

## Key models

- `pos.config`
- `pos.payment.method`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




