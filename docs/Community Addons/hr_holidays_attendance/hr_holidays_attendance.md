<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# HR Attendance Holidays

- Scope: Community Addons
- Source: odoo/addons/hr_holidays_attendance
- Dependencies: [[docs/Community Addons/hr_attendance/hr_attendance|hr_attendance]], [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

## Summary

Attendance Holidays

## Generated coverage

- Models: 9
- XML files with UI/data artifacts: 7
- Views: 12
- Actions: 2
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 0
- Frontend asset files: 2

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
title HR Attendance Holidays - Generated Coverage
component "Module Overview" as overview
component "Models\n9" as models
component "Views / XML\n12 views\n7 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/hr_holidays_attendance/Models|Models]] (9)
- Views and XML: [[docs/Community Addons/hr_holidays_attendance/Views|Views]] (7 files)
- Frontend: [[docs/Community Addons/hr_holidays_attendance/Frontend|Frontend]] (2 files)

## Key models

- `hr.attendance.overtime.line`
- `hr.attendance.overtime.rule`
- `hr.employee`
- `hr.leave`
- `hr.leave.accrual.level`
- `hr.leave.allocation`
- `hr.leave.attendance.report`
- `hr.leave.type`
- `ir.ui.menu`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






