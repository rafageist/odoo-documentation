<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# ESG

- Scope: Enterprise Addons
- Source: enterprise/esg
- Dependencies: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]], [[docs/Community Addons/web_hierarchy/web_hierarchy|web_hierarchy]]

## Summary

Calculate and report your company's Environmental, Social, and Governance impact.

## Generated coverage

- Models: 14
- XML files with UI/data artifacts: 11
- Views: 23
- Actions: 11
- Menus: 17
- Rules (ir.rule): 3
- Access CSV entries: 11
- Controller units: 1
- Frontend asset files: 27

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
title ESG - Generated Coverage
component "Module Overview" as overview
component "Models\n14" as models
component "Views / XML\n23 views\n11 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n27 files" as frontend
component "Security / Data\n3 rules\n11 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/esg/Models|Models]] (14)
- Views and XML: [[docs/Enterprise Addons/esg/Views|Views]] (11 files)
- Controllers: [[docs/Enterprise Addons/esg/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/esg/Frontend|Frontend]] (27 files)

## Key models

- `account.account`
- `account.move`
- `account.move.line`
- `esg.activity.type`
- `esg.assignation.line`
- `esg.carbon.emission.report`
- `esg.carbon.report.handler`
- `esg.database`
- `esg.emission.factor`
- `esg.emission.factor.line`
- `esg.emission.source`
- `esg.gas`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




