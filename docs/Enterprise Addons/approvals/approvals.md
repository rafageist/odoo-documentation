<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Approvals

- Scope: Enterprise Addons
- Source: enterprise/approvals
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/hr/hr|hr]], [[docs/Community Addons/product/product|product]]

## Summary

Create and validate approvals requests

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 7
- Views: 13
- Actions: 11
- Menus: 12
- Rules (ir.rule): 17
- Access CSV entries: 14
- Controller units: 0
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
title Approvals - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n13 views\n7 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n11 files" as frontend
component "Security / Data\n17 rules\n14 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/approvals/Models|Models]] (8)
- Views and XML: [[docs/Enterprise Addons/approvals/Views|Views]] (7 files)
- Frontend: [[docs/Enterprise Addons/approvals/Frontend|Frontend]] (11 files)

## Key models

- `approval.approver`
- `approval.category`
- `approval.category.approver`
- `approval.product.line`
- `approval.request`
- `ir.attachment`
- `mail.activity`
- `mail.activity.type`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




