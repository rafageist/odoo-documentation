<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Intrastat Reports

- Scope: Enterprise Addons
- Source: enterprise/account_intrastat
- Dependencies: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]

## Generated coverage

- Models: 12
- XML files with UI/data artifacts: 7
- Views: 22
- Actions: 2
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 2
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
title Intrastat Reports - Generated Coverage
component "Module Overview" as overview
component "Models\n12" as models
component "Views / XML\n22 views\n7 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n4 files" as frontend
component "Security / Data\n0 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_intrastat/Models|Models]] (12)
- Views and XML: [[docs/Enterprise Addons/account_intrastat/Views|Views]] (7 files)
- Frontend: [[docs/Enterprise Addons/account_intrastat/Frontend|Frontend]] (4 files)

## Key models

- `account.intrastat.code`
- `account.intrastat.goods.report.handler`
- `account.intrastat.report.handler`
- `account.intrastat.services.report.handler`
- `account.move`
- `account.move.line`
- `account.return`
- `account.return.type`
- `product.product`
- `product.template`
- `res.company`
- `res.config.settings`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





