<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Envia Shipping

- Scope: Enterprise Addons
- Source: enterprise/delivery_envia
- Dependencies: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[docs/Community Addons/base_address_extended/base_address_extended|base_address_extended]], [[docs/Community Addons/phone_validation/phone_validation|phone_validation]]

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 3
- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2
- Controller units: 0
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
title Envia Shipping - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n5 views\n3 files" as views
component "Controllers\n0 routes" as controllers
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

- Models: [[docs/Enterprise Addons/delivery_envia/Models|Models]] (3)
- Views and XML: [[docs/Enterprise Addons/delivery_envia/Views|Views]] (3 files)
- Frontend: [[docs/Enterprise Addons/delivery_envia/Frontend|Frontend]] (2 files)

## Key models

- `delivery.carrier`
- `envia.shipping.wizard`
- `stock.package.type`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




