<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Time Off

- Scope: Community Addons
- Source: odoo/addons/hr_holidays
- Dependencies: [[docs/Community Addons/hr/hr|hr]], [[docs/Community Addons/calendar/calendar|calendar]], [[docs/Community Addons/resource/resource|resource]]

## Summary

Allocate time off and follow leave requests

## Generated coverage

- Models: 27
- XML files with UI/data artifacts: 19
- Views: 70
- Actions: 42
- Menus: 19
- Rules (ir.rule): 26
- Access CSV entries: 27
- Controller units: 1
- Frontend asset files: 66

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
title Time Off - Generated Coverage
component "Module Overview" as overview
component "Models\n27" as models
component "Views / XML\n70 views\n19 files" as views
component "Controllers\n5 routes" as controllers
component "Frontend\n66 files" as frontend
component "Security / Data\n26 rules\n27 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/hr_holidays/Models|Models]] (27)
- Views and XML: [[docs/Community Addons/hr_holidays/Views|Views]] (19 files)
- Controllers: [[docs/Community Addons/hr_holidays/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/hr_holidays/Frontend|Frontend]] (66 files)

## Key models

- `calendar.event`
- `hr.department`
- `hr.departure.wizard`
- `hr.employee`
- `hr.employee.public`
- `hr.holidays.cancel.leave`
- `hr.holidays.summary.employee`
- `hr.leave`
- `hr.leave.accrual.level`
- `hr.leave.accrual.plan`
- `hr.leave.allocation`
- `hr.leave.allocation.generate.multi.wizard`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






