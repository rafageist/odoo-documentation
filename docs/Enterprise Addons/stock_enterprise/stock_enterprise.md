<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Stock enterprise

- Scope: Enterprise Addons
- Source: enterprise/stock_enterprise
- Dependencies: [[docs/Community Addons/stock/stock|stock]], [[docs/Enterprise Addons/web_cohort/web_cohort|web_cohort]], [[docs/Enterprise Addons/web_map/web_map|web_map]]

## Summary

Advanced features for Stock

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 5
- Views: 9
- Actions: 6
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 1
- Controller units: 0
- Frontend asset files: 4

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
title Stock enterprise - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n9 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n4 files" as frontend
component "Security / Data\n1 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/stock_enterprise/Models|Models]] (3)
- Views and XML: [[docs/Enterprise Addons/stock_enterprise/Views|Views]] (5 files)
- Frontend: [[docs/Enterprise Addons/stock_enterprise/Frontend|Frontend]] (4 files)

## Key models

- `res.company`
- `res.config.settings`
- `stock.report`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




