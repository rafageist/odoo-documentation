<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Skills Management

- Scope: Community Addons
- Source: odoo/addons/hr_skills
- Dependencies: [[docs/Community Addons/hr/hr|hr]]

## Summary

Manage skills, knowledge and resume of your employees

## Generated coverage

- Models: 14
- XML files with UI/data artifacts: 11
- Views: 36
- Actions: 11
- Menus: 9
- Rules (ir.rule): 11
- Access CSV entries: 20
- Controller units: 1
- Frontend asset files: 19

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
title Skills Management - Generated Coverage
component "Module Overview" as overview
component "Models\n14" as models
component "Views / XML\n36 views\n11 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n19 files" as frontend
component "Security / Data\n11 rules\n20 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/hr_skills/Models|Models]] (14)
- Views and XML: [[docs/Community Addons/hr_skills/Views|Views]] (11 files)
- Controllers: [[docs/Community Addons/hr_skills/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/hr_skills/Frontend|Frontend]] (19 files)

## Key models

- `hr.employee`
- `hr.employee.cv.wizard`
- `hr.employee.public`
- `hr.employee.skill`
- `hr.individual.skill.mixin`
- `hr.job`
- `hr.job.skill`
- `hr.resume.line`
- `hr.resume.line.type`
- `hr.skill`
- `hr.skill.level`
- `hr.skill.type`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






