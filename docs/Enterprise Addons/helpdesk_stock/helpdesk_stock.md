<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk Stock

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_stock
- Dependencies: [[docs/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]], [[docs/Community Addons/stock/stock|stock]]

## Summary

Project, Tasks, Stock

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 3
- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 0

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
title Helpdesk Stock - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n4 views\n3 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/helpdesk_stock/Models|Models]] (6)
- Views and XML: [[docs/Enterprise Addons/helpdesk_stock/Views|Views]] (3 files)

## Key models

- `helpdesk.sla.report.analysis`
- `helpdesk.ticket`
- `helpdesk.ticket.report.analysis`
- `stock.picking`
- `stock.return.picking`
- `stock.return.picking.line`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





