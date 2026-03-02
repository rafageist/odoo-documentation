<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Lunch

- Scope: Community Addons
- Source: odoo/addons/lunch
- Dependencies: [[docs/Community Addons/mail/mail|mail]]

## Summary

Handle lunch orders of your employees

## Generated coverage

- Models: 12
- XML files with UI/data artifacts: 11
- Views: 39
- Actions: 17
- Menus: 17
- Rules (ir.rule): 10
- Access CSV entries: 17
- Controller units: 1
- Frontend asset files: 11

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
title Lunch - Generated Coverage
component "Module Overview" as overview
component "Models\n12" as models
component "Views / XML\n39 views\n11 files" as views
component "Controllers\n6 routes" as controllers
component "Frontend\n11 files" as frontend
component "Security / Data\n10 rules\n17 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/lunch/Models|Models]] (12)
- Views and XML: [[docs/Community Addons/lunch/Views|Views]] (11 files)
- Controllers: [[docs/Community Addons/lunch/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/lunch/Frontend|Frontend]] (11 files)

## Key models

- `lunch.alert`
- `lunch.cashmove`
- `lunch.cashmove.report`
- `lunch.location`
- `lunch.order`
- `lunch.product`
- `lunch.product.category`
- `lunch.supplier`
- `lunch.topping`
- `res.company`
- `res.config.settings`
- `res.users`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






