<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Starshipit Shipping

- Scope: Enterprise Addons
- Source: enterprise/delivery_starshipit
- Dependencies: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 4
- Views: 5
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2
- Controller units: 1
- Frontend asset files: 2

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
title Starshipit Shipping - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n5 views\n4 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n0 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/delivery_starshipit/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/delivery_starshipit/Views|Views]] (4 files)
- Controllers: [[docs/Enterprise Addons/delivery_starshipit/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/delivery_starshipit/Frontend|Frontend]] (2 files)

## Key models

- `delivery.carrier`
- `starshipit.shipping.wizard`
- `stock.package.type`
- `stock.picking`
- `stock.return.picking`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




