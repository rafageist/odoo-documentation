
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Product Barcode Lookup

- Scope: Enterprise Addons
- Source: enterprise/product_barcodelookup
- Dependencies: [[docs/Community Addons/product/product|product]]

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 4
- Views: 3
- Actions: 2
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1
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
title Product Barcode Lookup - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n3 views\n4 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n1 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/product_barcodelookup/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/product_barcodelookup/Views|Views]] (4 files)
- Frontend: [[docs/Enterprise Addons/product_barcodelookup/Frontend|Frontend]] (2 files)

## Key models

- `ir.cron.trigger`
- `product.fetch.image.wizard`
- `product.product`
- `product.template`
- `res.config.settings`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


