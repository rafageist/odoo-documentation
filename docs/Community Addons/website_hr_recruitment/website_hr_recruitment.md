<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Online Jobs

- Scope: Community Addons
- Source: odoo/addons/website_hr_recruitment
- Dependencies: [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]], [[docs/Community Addons/website_mail/website_mail|website_mail]]

## Summary

Manage your online hiring process

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 5
- Views: 10
- Actions: 3
- Menus: 1
- Rules (ir.rule): 4
- Access CSV entries: 4
- Controller units: 1
- Frontend asset files: 11

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
title Online Jobs - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n10 views\n5 files" as views
component "Controllers\n6 routes" as controllers
component "Frontend\n11 files" as frontend
component "Security / Data\n4 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_hr_recruitment/Models|Models]] (5)
- Views and XML: [[docs/Community Addons/website_hr_recruitment/Views|Views]] (5 files)
- Controllers: [[docs/Community Addons/website_hr_recruitment/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/website_hr_recruitment/Frontend|Frontend]] (11 files)

## Key models

- `hr.applicant`
- `hr.department`
- `hr.job`
- `hr.recruitment.source`
- `website`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




