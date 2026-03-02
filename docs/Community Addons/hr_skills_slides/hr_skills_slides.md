<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Skills e-learning

- Scope: Community Addons
- Source: odoo/addons/hr_skills_slides
- Dependencies: [[docs/Community Addons/hr_skills/hr_skills|hr_skills]], [[docs/Community Addons/website_slides/website_slides|website_slides]]

## Summary

Add completed courses to resume of your employees

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 5
- Views: 8
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 1

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
title Skills e-learning - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n8 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/hr_skills_slides/Models|Models]] (5)
- Views and XML: [[docs/Community Addons/hr_skills_slides/Views|Views]] (5 files)
- Frontend: [[docs/Community Addons/hr_skills_slides/Frontend|Frontend]] (1 files)

## Key models

- `hr.employee`
- `hr.employee.public`
- `hr.resume.line`
- `slide.channel`
- `slide.channel.partner`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






