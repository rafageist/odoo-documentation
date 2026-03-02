<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Products & Pricelists

- Scope: Community Addons
- Source: odoo/addons/product
- Dependencies: base (not documented), [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/uom/uom|uom]]

## Generated coverage

- Models: 33
- XML files with UI/data artifacts: 20
- Views: 60
- Actions: 24
- Menus: 0
- Rules (ir.rule): 6
- Access CSV entries: 38
- Controller units: 3
- Frontend asset files: 23

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
title Products & Pricelists - Generated Coverage
component "Module Overview" as overview
component "Models\n33" as models
component "Views / XML\n60 views\n20 files" as views
component "Controllers\n4 routes" as controllers
component "Frontend\n23 files" as frontend
component "Security / Data\n6 rules\n38 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/product/Models|Models]] (33)
- Views and XML: [[docs/Community Addons/product/Views|Views]] (20 files)
- Controllers: [[docs/Community Addons/product/Controllers|Controllers]] (3)
- Frontend: [[docs/Community Addons/product/Frontend|Frontend]] (23 files)

## Key models

- `ir.attachment`
- `product.attribute`
- `product.attribute.custom.value`
- `product.attribute.value`
- `product.catalog.mixin`
- `product.category`
- `product.combo`
- `product.combo.item`
- `product.document`
- `product.label.layout`
- `product.pricelist`
- `product.pricelist.item`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






