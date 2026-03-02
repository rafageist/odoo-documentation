<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Social X

- Scope: Enterprise Addons
- Source: enterprise/social_twitter
- Dependencies: [[docs/Enterprise Addons/social/social|social]], [[docs/Community Addons/iap/iap|iap]]

## Summary

Manage your X accounts and schedule posts

## Generated coverage

- Models: 9
- XML files with UI/data artifacts: 4
- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2
- Controller units: 1
- Frontend asset files: 10

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
title Social X - Generated Coverage
component "Module Overview" as overview
component "Models\n9" as models
component "Views / XML\n4 views\n4 files" as views
component "Controllers\n8 routes" as controllers
component "Frontend\n10 files" as frontend
component "Security / Data\n0 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/social_twitter/Models|Models]] (9)
- Views and XML: [[docs/Enterprise Addons/social_twitter/Views|Views]] (4 files)
- Controllers: [[docs/Enterprise Addons/social_twitter/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/social_twitter/Frontend|Frontend]] (10 files)

## Key models

- `res.config.settings`
- `social.account`
- `social.live.post`
- `social.media`
- `social.post`
- `social.post.template`
- `social.stream`
- `social.stream.post`
- `social.twitter.account`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




