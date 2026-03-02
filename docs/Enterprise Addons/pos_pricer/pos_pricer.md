<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# PoS Pricer

- Scope: Enterprise Addons
- Source: enterprise/pos_pricer
- Dependencies: [[docs/Community Addons/product/product|product]], [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Display and change your products information on electronic Pricer tags

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 4
- Views: 5
- Actions: 2
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 2
- Controller units: 0
- Frontend asset files: 1

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
title PoS Pricer - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n5 views\n4 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/pos_pricer/Models|Models]] (6)
- Views and XML: [[docs/Enterprise Addons/pos_pricer/Views|Views]] (4 files)
- Frontend: [[docs/Enterprise Addons/pos_pricer/Frontend|Frontend]] (1 files)

## Key models

- `pos.config`
- `pricer.store`
- `pricer.tag`
- `product.product`
- `product.template`
- `stock.move`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





