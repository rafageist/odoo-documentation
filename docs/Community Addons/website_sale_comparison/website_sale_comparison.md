<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Product Comparison

- Scope: Community Addons
- Source: odoo/addons/website_sale_comparison
- Dependencies: [[docs/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Allow shoppers to compare products based on their attributes

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 1
- Views: 3
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 4
- Controller units: 1
- Frontend asset files: 9

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
title Product Comparison - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n3 views\n1 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n9 files" as frontend
component "Security / Data\n0 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_sale_comparison/Models|Models]] (4)
- Views and XML: [[docs/Community Addons/website_sale_comparison/Views|Views]] (1 files)
- Controllers: [[docs/Community Addons/website_sale_comparison/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/website_sale_comparison/Frontend|Frontend]] (9 files)

## Key models

- `product.attribute`
- `product.attribute.category`
- `product.product`
- `product.template.attribute.line`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




