<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Appraisal - Survey

- Scope: Enterprise Addons
- Source: enterprise/hr_appraisal_survey
- Dependencies: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]], [[docs/Community Addons/survey/survey|survey]]

## Summary

360 Feedback

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 7
- Views: 9
- Actions: 2
- Menus: 1
- Rules (ir.rule): 11
- Access CSV entries: 13
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
title Appraisal - Survey - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n9 views\n7 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n11 rules\n13 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/hr_appraisal_survey/Models|Models]] (7)
- Views and XML: [[docs/Enterprise Addons/hr_appraisal_survey/Views|Views]] (7 files)
- Controllers: [[docs/Enterprise Addons/hr_appraisal_survey/Controllers|Controllers]] (1)

## Key models

- `appraisal.ask.feedback`
- `appraisal.select.survey`
- `hr.appraisal`
- `hr.appraisal.template`
- `survey.question.answer`
- `survey.survey`
- `survey.user_input`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




