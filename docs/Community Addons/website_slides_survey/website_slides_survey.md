<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Course Certifications

- Scope: Community Addons
- Source: odoo/addons/website_slides_survey
- Dependencies: [[docs/Community Addons/website_slides/website_slides|website_slides]], [[docs/Community Addons/survey/survey|survey]]

## Summary

Add certification capabilities to your courses

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 8
- Views: 12
- Actions: 5
- Menus: 1
- Rules (ir.rule): 5
- Access CSV entries: 5
- Controller units: 1
- Frontend asset files: 6

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
title Course Certifications - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n12 views\n8 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n6 files" as frontend
component "Security / Data\n5 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_slides_survey/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/website_slides_survey/Views|Views]] (8 files)
- Controllers: [[docs/Community Addons/website_slides_survey/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/website_slides_survey/Frontend|Frontend]] (6 files)

## Key models

- `slide.channel`
- `slide.channel.partner`
- `slide.slide`
- `slide.slide.partner`
- `survey.survey`
- `survey.user_input`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




