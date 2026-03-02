<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Social Demo Module

- Scope: Enterprise Addons
- Source: enterprise/social_demo
- Dependencies: [[docs/Enterprise Addons/social/social|social]], [[docs/Enterprise Addons/social_facebook/social_facebook|social_facebook]], [[docs/Enterprise Addons/social_twitter/social_twitter|social_twitter]], [[docs/Enterprise Addons/social_linkedin/social_linkedin|social_linkedin]], [[docs/Enterprise Addons/social_youtube/social_youtube|social_youtube]], [[docs/Enterprise Addons/social_instagram/social_instagram|social_instagram]], [[docs/Community Addons/product/product|product]]

## Summary

Get demo data for the social module

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 0
- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 0
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
title Social Demo Module - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n0 views\n0 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/social_demo/Models|Models]] (6)
- Frontend: [[docs/Enterprise Addons/social_demo/Frontend|Frontend]] (3 files)

## Key models

- `social.account`
- `social.live.post`
- `social.post`
- `social.stream`
- `social.stream.post`
- `utm.campaign`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




