
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sale Accounting

- Scope: Enterprise Addons
- Source: enterprise/sale_account_accountant
- Dependencies: [[docs/Community Addons/sale/sale|sale]], [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]]

## Summary

Bridge between Sale and Accounting

## Generated coverage

- Models: 1
- XML files with UI/data artifacts: 1
- Views: 2
- Actions: 2
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 0
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
title Sale Accounting - Generated Coverage
component "Module Overview" as overview
component "Models\n1" as models
component "Views / XML\n2 views\n1 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/sale_account_accountant/Models|Models]] (1)
- Views and XML: [[docs/Enterprise Addons/sale_account_accountant/Views|Views]] (1 files)
- Frontend: [[docs/Enterprise Addons/sale_account_accountant/Frontend|Frontend]] (1 files)

## Key models

- `sale.order.line`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


