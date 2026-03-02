<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Social Marketing

- Scope: Enterprise Addons
- Source: enterprise/social
- Dependencies: [[docs/Community Addons/web/web|web]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/iap/iap|iap]], [[docs/Community Addons/link_tracker/link_tracker|link_tracker]]

## Summary

Manage your social media and website visitors

## Generated coverage

- Models: 13
- XML files with UI/data artifacts: 11
- Views: 23
- Actions: 8
- Menus: 15
- Rules (ir.rule): 12
- Access CSV entries: 21
- Controller units: 0
- Frontend asset files: 24

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
title Social Marketing - Generated Coverage
component "Module Overview" as overview
component "Models\n13" as models
component "Views / XML\n23 views\n11 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n24 files" as frontend
component "Security / Data\n12 rules\n21 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/social/Models|Models]] (13)
- Views and XML: [[docs/Enterprise Addons/social/Views|Views]] (11 files)
- Frontend: [[docs/Enterprise Addons/social/Frontend|Frontend]] (24 files)

## Key models

- `res.config.settings`
- `social.account`
- `social.live.post`
- `social.media`
- `social.post`
- `social.post.template`
- `social.stream`
- `social.stream.post`
- `social.stream.post.image`
- `social.stream.type`
- `utm.campaign`
- `utm.medium`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




