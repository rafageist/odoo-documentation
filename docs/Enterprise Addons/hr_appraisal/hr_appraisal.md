<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Appraisals

- Scope: Enterprise Addons
- Source: enterprise/hr_appraisal
- Dependencies: [[docs/Community Addons/calendar/calendar|calendar]], [[docs/Enterprise Addons/hr_gantt/hr_gantt|hr_gantt]]

## Summary

Assess your employees

## Generated coverage

- Models: 15
- XML files with UI/data artifacts: 13
- Views: 37
- Actions: 18
- Menus: 12
- Rules (ir.rule): 14
- Access CSV entries: 15
- Controller units: 0
- Frontend asset files: 30

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
title Appraisals - Generated Coverage
component "Module Overview" as overview
component "Models\n15" as models
component "Views / XML\n37 views\n13 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n30 files" as frontend
component "Security / Data\n14 rules\n15 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/hr_appraisal/Models|Models]] (15)
- Views and XML: [[docs/Enterprise Addons/hr_appraisal/Views|Views]] (13 files)
- Frontend: [[docs/Enterprise Addons/hr_appraisal/Frontend|Frontend]] (30 files)

## Key models

- `hr.appraisal`
- `hr.appraisal.campaign.wizard`
- `hr.appraisal.goal`
- `hr.appraisal.goal.tag`
- `hr.appraisal.note`
- `hr.appraisal.template`
- `hr.department`
- `hr.departure.wizard`
- `hr.employee`
- `hr.employee.public`
- `mail.template`
- `request.appraisal`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




