<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Hr Recruitment Extract

- Scope: Enterprise Addons
- Source: enterprise/hr_recruitment_extract
- Dependencies: [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]], [[docs/Enterprise Addons/iap_extract/iap_extract|iap_extract]], [[docs/Community Addons/iap_mail/iap_mail|iap_mail]], [[docs/Enterprise Addons/mail_enterprise/mail_enterprise|mail_enterprise]]

## Summary

Extract data from CV scans to fill applicant forms automatically

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 3
- Views: 3
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
- Frontend asset files: 3

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
title Hr Recruitment Extract - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n3 views\n3 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/hr_recruitment_extract/Models|Models]] (3)
- Views and XML: [[docs/Enterprise Addons/hr_recruitment_extract/Views|Views]] (3 files)
- Controllers: [[docs/Enterprise Addons/hr_recruitment_extract/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/hr_recruitment_extract/Frontend|Frontend]] (3 files)

## Key models

- `hr.applicant`
- `res.company`
- `res.config.settings`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





