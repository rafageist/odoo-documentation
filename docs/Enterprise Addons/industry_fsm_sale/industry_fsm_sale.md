<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Field Service - Sale

- Scope: Enterprise Addons
- Source: enterprise/industry_fsm_sale
- Dependencies: [[docs/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]], [[docs/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]]

## Summary

Schedule and track onsite operations, invoice time and material

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 6
- Views: 15
- Actions: 21
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 2
- Frontend asset files: 7

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
title Field Service - Sale - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n15 views\n6 files" as views
component "Controllers\n4 routes" as controllers
component "Frontend\n7 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/industry_fsm_sale/Models|Models]] (10)
- Views and XML: [[docs/Enterprise Addons/industry_fsm_sale/Views|Views]] (6 files)
- Controllers: [[docs/Enterprise Addons/industry_fsm_sale/Controllers|Controllers]] (2)
- Frontend: [[docs/Enterprise Addons/industry_fsm_sale/Frontend|Frontend]] (7 files)

## Key models

- `account.analytic.line`
- `product.product`
- `product.template`
- `project.project`
- `project.sale.line.employee.map`
- `project.task`
- `report.project.task.user.fsm`
- `sale.advance.payment.inv`
- `sale.order`
- `sale.order.line`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




