<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk FSM

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_fsm
- Dependencies: [[docs/Enterprise Addons/project_helpdesk/project_helpdesk|project_helpdesk]], [[docs/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]]

## Summary

Allow generating fsm tasks from ticket

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 5
- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 1
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
title Helpdesk FSM - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n5 views\n5 files" as views
component "Controllers\n1 routes" as controllers
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

- Models: [[docs/Enterprise Addons/helpdesk_fsm/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/helpdesk_fsm/Views|Views]] (5 files)
- Controllers: [[docs/Enterprise Addons/helpdesk_fsm/Controllers|Controllers]] (1)

## Key models

- `helpdesk.create.fsm.task`
- `helpdesk.team`
- `helpdesk.ticket`
- `helpdesk.ticket.convert.wizard`
- `project.task`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




