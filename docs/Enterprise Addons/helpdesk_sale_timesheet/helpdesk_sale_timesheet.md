<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sell Helpdesk Timesheet

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_sale_timesheet
- Dependencies: [[docs/Enterprise Addons/helpdesk_timesheet/helpdesk_timesheet|helpdesk_timesheet]], [[docs/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]], [[docs/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]]

## Summary

Project, Helpdesk, Timesheet and Sale Orders

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 8
- Views: 10
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1
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
title Sell Helpdesk Timesheet - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n10 views\n8 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/helpdesk_sale_timesheet/Models|Models]] (10)
- Views and XML: [[docs/Enterprise Addons/helpdesk_sale_timesheet/Views|Views]] (8 files)

## Key models

- `account.analytic.line`
- `helpdesk.sla`
- `helpdesk.sla.report.analysis`
- `helpdesk.team`
- `helpdesk.ticket`
- `helpdesk.ticket.convert.wizard`
- `helpdesk.ticket.report.analysis`
- `project.task.convert.wizard`
- `sale.order`
- `sale.order.line`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





