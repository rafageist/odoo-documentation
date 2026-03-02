<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Equity

- Scope: Enterprise Addons
- Source: enterprise/equity
- Dependencies: [[docs/Community Addons/portal/portal|portal]]

## Summary

Manage securities, transactions, and cap tables.

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 9
- Views: 16
- Actions: 11
- Menus: 12
- Rules (ir.rule): 2
- Access CSV entries: 14
- Controller units: 1
- Frontend asset files: 16

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
title Equity - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n16 views\n9 files" as views
component "Controllers\n5 routes" as controllers
component "Frontend\n16 files" as frontend
component "Security / Data\n2 rules\n14 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/equity/Models|Models]] (6)
- Views and XML: [[docs/Enterprise Addons/equity/Views|Views]] (9 files)
- Controllers: [[docs/Enterprise Addons/equity/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/equity/Frontend|Frontend]] (16 files)

## Key models

- `equity.cap.table`
- `equity.security.class`
- `equity.transaction`
- `equity.ubo`
- `equity.valuation`
- `res.partner`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




