<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Job Board - Monster.com

- Scope: Enterprise Addons
- Source: enterprise/hr_recruitment_integration_monster
- Dependencies: [[docs/Enterprise Addons/hr_recruitment_integration_base/hr_recruitment_integration_base|hr_recruitment_integration_base]], [[docs/Enterprise Addons/hr_recruitment_extract/hr_recruitment_extract|hr_recruitment_extract]]

## Summary

Allow user to share job positions on Monster Job board

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 4
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
title Job Board - Monster.com - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n4 views\n4 files" as views
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

- Models: [[docs/Enterprise Addons/hr_recruitment_integration_monster/Models|Models]] (8)
- Views and XML: [[docs/Enterprise Addons/hr_recruitment_integration_monster/Views|Views]] (4 files)

## Key models

- `hr.contract.type`
- `hr.job.post`
- `hr.recruitment.platform`
- `hr.recruitment.post.job.wizard`
- `res.company`
- `res.config.settings`
- `res.currency`
- `res.partner.industry`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




